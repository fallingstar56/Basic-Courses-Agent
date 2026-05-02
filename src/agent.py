"""基于 Kimi K2.5 + RAG 的数学解题智能体。"""

import json
import re
import logging
from typing import Any, Dict, List, Optional

from openai import OpenAI

from config import KIMI_API_KEY, KIMI_BASE_URL, MODEL_NAME, MAX_TOOL_RETRIES, CODE_EXEC_TIMEOUT
from tool_executor import run_python_code
from rag import ExampleRetriever
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# 工具定义（Function Calling）
TOOL_DEFINITION = [
    {
        "type": "function",
        "function": {
            "name": "python_exec",
            "description": "执行 Python 代码，用于数学计算、符号推导、数值验证等。代码中可以使用 print 输出结果。禁止执行危险操作。",
            "parameters": {
                "type": "object",
                "properties": {
                    "code": {
                        "type": "string",
                        "description": "要执行的 Python 代码。使用 print() 输出需要的结果。",
                    }
                },
                "required": ["code"],
            },
        },
    }
]

# 基础系统提示（不含示例）
BASE_SYSTEM_PROMPT = """\
你是一个大学数学解题助手，精通微积分、线性代数、大学物理、电路原理等课程。
你的任务是对给出的题目进行逐步推理，并最终给出准确答案。
要求：
1. 推理过程（reasoning_process）必须详细、逻辑严密，包含必要的公式和步骤。
2. 当需要计算数值、求解方程、积分、导数，或进行数值验证时，可以调用 `python_exec` 工具来执行 Python 代码。
    - 代码中只能使用 print 输出结果，不要调用 input、文件读写或危险模块。
    - 对于符号运算（如求导、积分、极限），可调用 sympy（假设环境中已安装）。
3. 如果题目是证明题，主要依靠逻辑推导，必要时可用代码辅助计算特定项或不等式验证。
4. 最终输出的 answer 应简洁明确，与题目要求的答案格式一致。
5. 如果题目包含歧义、超过课程范围，请在推理中说明，并尝试给出合理回应；若完全无法解答，请说明原因。
"""

class MathAgent:
    """解题智能体，通过调用 Kimi K2.5 + RAG 完成题目解答。"""

    def __init__(self, example_json_path: str = "combined_result_examples.json"):
        self.client = OpenAI(
            api_key=KIMI_API_KEY,
            base_url=KIMI_BASE_URL,
        )
        self.model = MODEL_NAME
        self.retriever = ExampleRetriever(example_json_path)

    def _build_system_prompt(self, query: str, q_type: str) -> str:
        """根据当前问题检索相似示例，并嵌入系统提示。"""
        similar_examples = self.retriever.retrieve(query, top_k=2)  # 取前2个最相似的示例
        prompt = BASE_SYSTEM_PROMPT
        if similar_examples:
            prompt += "\n\n## 参考示例（来自教材/习题库，可借鉴其推理风格）\n"
            for i, (ex, sim) in enumerate(similar_examples, 1):
                prompt += f"\n[示例 {i}] (相似度: {sim:.2f})\n"
                prompt += f"题目: {ex['question']}\n"
                prompt += f"答案: {ex['answer']}\n"
        return prompt

    def solve(self, item: Dict[str, Any]) -> Dict[str, str]:
        # ---------- 1. 输入校验 ----------
        required_fields = ["question_id"]
        for field in required_fields:
            if field not in item:
                return {
                    "question_id": item.get("question_id", "unknown"),
                    "reasoning_process": f"输入缺少必要字段：{field}",
                    "answer": "[输入格式错误]",
                }

        q_id = str(item.get("question_id", ""))
        q_type = item.get("type", "未知类型")
        difficulty = item.get("difficulty", "未知难度")
        question = item.get("question", "").strip()
        image_path = item.get("image")  # 暂不处理图像

        if not question:
            return {
                "question_id": q_id,
                "reasoning_process": "题目文本为空，无法解答。",
                "answer": "[题目为空]",
            }

        # ---------- 2. 构建系统提示（含 RAG 示例） ----------
        system_prompt = self._build_system_prompt(question, q_type)

        user_content = f"""题目类型: {q_type}
难度: {difficulty}
题目内容:
{question}
"""
        if image_path:
            user_content += f"\n[提示] 题目包含图片: {image_path}，当前版本不支持图片解析，请仅根据文字部分作答。"

        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_content},
        ]

        # ---------- 3. 多轮工具调用循环 ----------
        # 第一次调用
        retries = MAX_TOOL_RETRIES
        while retries > 0:
            try:
                response = self.client.chat.completions.create(
                    model=self.model,
                    messages=messages,
                    tools=TOOL_DEFINITION,
                    tool_choice="auto",
                )
                break
            except Exception as e:
                retries -= 1
                logger.warning(f"API 调用失败，剩余重试 {retries} 次: {e}")
                if retries == 0:
                    return self._fallback_solve(item)

        assistant_message = response.choices[0].message
        messages.append(assistant_message)

        max_turns = 5
        for _ in range(max_turns):
            if not assistant_message.tool_calls:
                # 没有工具调用，模型直接给出最终答复
                break

            # 处理每个工具调用
            for tool_call in assistant_message.tool_calls:
                if tool_call.function.name != "python_exec":
                    tool_response = {"role": "tool", "content": "未知工具", "tool_call_id": tool_call.id}
                else:
                    try:
                        code = json.loads(tool_call.function.arguments)["code"]
                        stdout, stderr = run_python_code(code, timeout=CODE_EXEC_TIMEOUT)
                        if stderr:
                            tool_response_content = f"执行错误:\n{stderr}\n标准输出:\n{stdout}"
                        else:
                            tool_response_content = stdout if stdout else "执行成功（无输出）"
                    except Exception as e:
                        tool_response_content = f"工具调用解析失败: {str(e)}"
                    tool_response = {
                        "role": "tool",
                        "content": tool_response_content,
                        "tool_call_id": tool_call.id,
                    }
                messages.append(tool_response)

            # 再次调用模型
            retries = MAX_TOOL_RETRIES
            while retries > 0:
                try:
                    response = self.client.chat.completions.create(
                        model=self.model,
                        messages=messages,
                        tools=TOOL_DEFINITION,
                        tool_choice="auto",
                    )
                    break
                except Exception as e:
                    retries -= 1
                    logger.warning(f"API 二次调用失败，剩余重试 {retries} 次: {e}")
                    if retries == 0:
                        return self._fallback_solve(item)
            assistant_message = response.choices[0].message
            messages.append(assistant_message)

        # ---------- 4. 提取最终答案 ----------
        final_content = assistant_message.content or ""
        answer, reasoning = self._parse_final_output(final_content)
        if not reasoning:
            reasoning = final_content
        if not answer:
            answer = self._extract_answer_from_text(reasoning)

        return {
            "question_id": q_id,
            "reasoning_process": reasoning.strip()[:2000],  # 限制长度
            "answer": str(answer).strip(),
        }

    def _parse_final_output(self, content: str) -> (str, str):
        """尝试从模型输出中分离答案和推理过程。"""
        answer = ""
        reasoning = content
        # 匹配类似 "最终答案：..." 或 "答案：..." 或 \boxed{...}
        patterns = [
            r"最终[答案|结果][：:]\s*(.*?)$",
            r"[答案|结果][：:]\s*(.*?)$",
            r"\\boxed{(.*?)}",
        ]
        for pat in patterns:
            match = re.search(pat, content, re.MULTILINE | re.DOTALL)
            if match:
                answer = match.group(1).strip()
                break
        return answer, reasoning

    def _extract_answer_from_text(self, text: str) -> str:
        """简单的后备方案：取最后一行作为答案。"""
        lines = text.strip().split("\n")
        if lines:
            return lines[-1].strip()
        return "[未提取到答案]"

    def _fallback_solve(self, item: Dict[str, Any]) -> Dict[str, str]:
        """当 LLM 调用全部失败时，使用原始 baseline 逻辑降级。"""
        print("调用LLM失败，请重试")
