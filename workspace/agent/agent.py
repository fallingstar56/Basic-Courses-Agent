"""基于 Kimi K2.5 + RAG 的数学解题智能体，支持多模态图片输入。"""
import json
import re
import logging
import base64
import os
import time
from typing import Any, Dict, List, Optional, Tuple

from openai import OpenAI

from config import (KIMI_API_KEY, KIMI_BASE_URL, MODEL_NAME,
                    MAX_TOOL_RETRIES, CODE_EXEC_TIMEOUT,
                    AVAILABLE_SUBJECTS)
from tool_executor import run_python_code
from rag import RAGRetriever

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)
logging.getLogger("httpx").setLevel(logging.WARNING)
logging.getLogger("openai").setLevel(logging.WARNING)

TOOL_DEFINITION = [
    {
        "type": "function",
        "function": {
            "name": "python_exec",
            "description": "执行 Python 代码，用于数学计算、符号推导、数值验证等。使用 print 输出结果，已提供 sympy 和 math 库。",
            "parameters": {
                "type": "object",
                "properties": {
                    "code": {"type": "string", "description": "要执行的 Python 代码。使用 print() 输出需要的结果。"}
                },
                "required": ["code"],
            },
        },
    }
]

BASE_SYSTEM_PROMPT = """\
你是一个清华大学理工科基础课程解题助手，精通基础物理学、电路原理、线性代数、微积分等课程。
你的任务是对给出的题目进行逐步推理，并最终给出准确答案。
要求：
1. 推理过程（reasoning_process）必须详细、逻辑严密，包含必要的公式和步骤。
2. 推理过程请控制在 800 字以内，清晰展现解题思路。
3. 当需要计算数值、求解方程、求极限积分，或进行数值验证时，必须调用 `python_exec` 工具执行 Python 代码。
    - 代码中只能使用 print 输出结果，不要调用 input 或危险模块。
    - 对于符号运算（如求导、积分、极限），可调用 sympy（环境中已安装）。
4. 最终输出的 answer 应简洁明确。数值计算/填空题只输出数值或带单位的结果；计算题/证明题给出简明步骤。
5. 如果题目包含歧义或超出课程范围，请在推理中说明；若完全无法解答，请说明原因。
"""


class MathAgent:
    """解题智能体，通过调用 Kimi K2.5 + RAG 完成题目解答。"""

    def __init__(self,
                 rag_data_dir: Optional[str] = None,
                 subjects: Optional[List[str]] = AVAILABLE_SUBJECTS):
        self.client = OpenAI(api_key=KIMI_API_KEY, base_url=KIMI_BASE_URL)
        self.model = MODEL_NAME
        
        # 【关键增强】不依赖外部环境变量，绝对精准定位内部的 rag 文件夹
        if not rag_data_dir:
            # 找到 agent.py 当前所在的绝对目录（即 agent 文件夹）
            current_dir = os.path.dirname(os.path.abspath(__file__))
            # 直接拼接内部的 rag 文件夹
            rag_data_dir = os.path.join(current_dir, "rag")
            
        self.rag_data_dir = rag_data_dir
        self.subjects = subjects or []
        
        # 初始化 RAG Retriever，不再惧怕路径或编码错误
        self.retriever = RAGRetriever(self.rag_data_dir, self.subjects)

    def _build_system_prompt(self, query: str, q_type: str) -> str:
        know_texts, examples = self.retriever.retrieve(query, know_top_k=2, exam_top_k=2)
        prompt = BASE_SYSTEM_PROMPT

        if know_texts:
            prompt += "\n\n## 相关知识（来自教材/讲义）\n"
            for i, text in enumerate(know_texts, 1):
                truncated = text[:1500] + ("..." if len(text) > 1500 else "")
                prompt += f"\n[知识 {i}]:\n{truncated}\n"

        if examples:
            prompt += "\n## 参考示例（来自习题库）\n"
            for i, (ex, sim) in enumerate(examples, 1):
                prompt += f"\n[示例 {i}] (相似度: {sim:.2f})\n"
                prompt += f"题目: {ex.get('question', '')}\n"
                reasoning = ex.get('reasoning_process', ex.get('answer', ''))
                if reasoning:
                    prompt += f"思考过程: {reasoning}\n"
                answer = ex.get('answer', '')
                if answer:
                    prompt += f"答案: {answer}\n"

        return prompt

    def _encode_image(self, image_path: str) -> Optional[str]:
        try:
            with open(image_path, "rb") as f:
                return base64.b64encode(f.read()).decode('utf-8')
        except Exception as e:
            logger.warning(f"无法读取图片 {image_path}: {e}")
            return None

    def _resolve_image_path(self, raw_path: str) -> Optional[str]:
        # 1. 如果评测机给的是绝对路径，或者相对于评测运行脚本的当前目录直接存在
        if os.path.exists(raw_path):
            return raw_path
            
        # 2. 从我们自带的 rag 知识库内部所有可能目录兜底寻找
        search_dirs = [os.getcwd(), self.rag_data_dir]
        for subj in self.subjects:
            search_dirs.append(os.path.join(self.rag_data_dir, subj))
            
        for d in search_dirs:
            candidate = os.path.join(d, raw_path)
            if os.path.exists(candidate):
                return candidate
        return None

    def solve(self, item: Dict[str, Any]) -> Dict[str, str]:
        # 1. 输入校验
        q_id = str(item.get("question_id", ""))
        q_type = item.get("type", "未知类型")
        difficulty = item.get("difficulty", "未知难度")
        question = item.get("question", "").strip()
        image_raw = item.get("image")

        # 尝试通过正则在文本中自动提取图片，增加多模态稳健性
        if not image_raw:
            img_match = re.search(r'<img\s+[^>]*src=["\']([^"\']+)["\']', question)
            if img_match:
                image_raw = img_match.group(1)

        if not question:
            return {
                "question_id": q_id,
                "reasoning_process": "题目文本为空，无法解答。",
                "answer": "[题目为空]",
            }

        # 2. 构建系统提示
        system_prompt = self._build_system_prompt(question, q_type)

        # 3. 构造用户消息
        if image_raw:
            image_path = self._resolve_image_path(str(image_raw))
            if image_path:
                b64_img = self._encode_image(image_path)
                if b64_img:
                    ext = os.path.splitext(image_path)[1].lower()
                    mime_map = {
                        '.jpg': 'image/jpeg', '.jpeg': 'image/jpeg',
                        '.png': 'image/png', '.gif': 'image/gif',
                        '.webp': 'image/webp', '.bmp': 'image/bmp',
                    }
                    mime_type = mime_map.get(ext, 'image/jpeg')
                    image_url = f"data:{mime_type};base64,{b64_img}"
                    user_content = [
                        {"type": "text", "text": f"题目类型: {q_type}\n难度: {difficulty}\n题目内容:\n{question}"},
                        {"type": "image_url", "image_url": {"url": image_url}}
                    ]
                else:
                    user_content = f"题目类型: {q_type}\n难度: {difficulty}\n题目内容:\n{question}\n\n[提示] 图片读取失败，请根据文字作答。"
            else:
                user_content = f"题目类型: {q_type}\n难度: {difficulty}\n题目内容:\n{question}\n\n[提示] 未找到图片 {image_raw}，请根据文字部分作答。"
        else:
            user_content = f"题目类型: {q_type}\n难度: {difficulty}\n题目内容:\n{question}"

        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_content},
        ]

        # 4. 初次 API 调用（带指数退避）
        for attempt in range(1, MAX_TOOL_RETRIES + 1):
            try:
                response = self.client.chat.completions.create(
                    model=self.model,
                    messages=messages,
                    tools=TOOL_DEFINITION,
                    tool_choice="auto",
                )
                break
            except Exception as e:
                wait_time = 2 ** attempt
                logger.warning(f"API 调用失败 (尝试 {attempt}/{MAX_TOOL_RETRIES})，{wait_time}秒后重试: {e}")
                time.sleep(wait_time)
                if attempt == MAX_TOOL_RETRIES:
                    return self._fallback_solve(item)
        else:
            return self._fallback_solve(item)

        assistant_message = response.choices[0].message
        messages.append(assistant_message)

        # 5. 工具调用循环
        max_turns = 5
        for _ in range(max_turns):
            if not assistant_message.tool_calls:
                break

            for tool_call in assistant_message.tool_calls:
                if tool_call.function.name != "python_exec":
                    tool_response = {"role": "tool", "content": "未知工具", "tool_call_id": tool_call.id}
                else:
                    try:
                        # 兼容 Kimi 可能返回的 ```json 包裹格式
                        raw_args = tool_call.function.arguments
                        raw_args = re.sub(r'^```json\s*', '', raw_args)
                        raw_args = re.sub(r'\s*```$', '', raw_args)
                        
                        code = json.loads(raw_args).get("code", "")
                        stdout, stderr = run_python_code(code, timeout=CODE_EXEC_TIMEOUT)
                        if stderr:
                            tool_response_content = f"执行错误:\n{stderr}\n标准输出:\n{stdout}"
                        else:
                            tool_response_content = stdout if stdout else "执行成功（无输出）"
                    except Exception as e:
                        tool_response_content = f"工具参数解析失败: {str(e)}"
                        
                    tool_response = {
                        "role": "tool",
                        "content": tool_response_content,
                        "tool_call_id": tool_call.id,
                    }
                messages.append(tool_response)

            for attempt in range(1, MAX_TOOL_RETRIES + 1):
                try:
                    response = self.client.chat.completions.create(
                        model=self.model,
                        messages=messages,
                        tools=TOOL_DEFINITION,
                        tool_choice="auto",
                    )
                    break
                except Exception as e:
                    wait_time = 2 ** attempt
                    logger.warning(f"API 二次调用失败 (尝试 {attempt}/{MAX_TOOL_RETRIES})，{wait_time}秒后重试: {e}")
                    time.sleep(wait_time)
                    if attempt == MAX_TOOL_RETRIES:
                        return self._fallback_solve(item)
            else:
                return self._fallback_solve(item)

            assistant_message = response.choices[0].message
            messages.append(assistant_message)

        # 6. 提取最终答案
        final_content = assistant_message.content or ""
        answer, reasoning = self._parse_final_output(final_content)
        if not reasoning:
            reasoning = final_content
        if not answer or re.fullmatch(r'\**\s*', answer):
            answer = self._extract_answer_from_text(reasoning)

        return {
            "question_id": q_id,
            "reasoning_process": reasoning.strip()[:2000],
            "answer": str(answer).strip(),
        }

    def _clean_answer(self, raw: str) -> str:
        ans = raw.strip()
        if ans.startswith("**") and ans.endswith("**"):
            ans = ans[2:-2].strip()
        ans = re.sub(r'\\boxed\{(.*)\}', r'\1', ans).strip()
        return ans

    def _parse_final_output(self, content: str) -> Tuple[str, str]:
        answer = ""
        reasoning = content
        patterns = [
            r"(?:最终\s*)?答案\s*[：:]\s*(.+?)$",
            r"(?:最终\s*)?结果\s*[：:]\s*(.+?)$",
            r"\\boxed\{(.+?)\}",
        ]
        for pat in patterns:
            match = re.search(pat, content, re.MULTILINE | re.IGNORECASE)
            if match:
                answer = self._clean_answer(match.group(1))
                break
        return answer, reasoning

    def _extract_answer_from_text(self, text: str) -> str:
        lines = text.strip().split("\n")
        if lines:
            last = lines[-1].strip()
            m = re.match(r"(?:答案|结果)[：:]\s*(.*)", last)
            if m:
                return self._clean_answer(m.group(1))
            return last
        return "[未提取到答案]"

    def _fallback_solve(self, item: Dict[str, Any]) -> Dict[str, str]:
        return {
            "question_id": str(item.get("question_id", "")),
            "reasoning_process": "由于模型API临时不可用或运行超时，无法得出解答。",
            "answer": "[API 调用失败]",
        }