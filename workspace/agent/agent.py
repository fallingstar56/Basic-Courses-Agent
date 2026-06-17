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
                    API_TIMEOUT_SECONDS, MAX_OUTPUT_TOKENS,
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
1. reasoning_process 必须写成面向人的自然语言做题过程，包含必要的条件分析、公式引用和关键计算，不要写成大模型内部流程、策略说明或元叙述。
2. reasoning_process 请控制在 800 字以内，清晰、连贯地展现解题思路。
3. 当需要计算数值、求解方程、求极限积分，或进行数值验证时，必须调用 `python_exec` 工具执行 Python 代码。
    - 代码中只能使用 print 输出结果，不要调用 input 或危险模块。
    - 对于符号运算（如求导、积分、极限），可调用 sympy（环境中已安装）。
    - 工具只用于辅助计算；获得工具结果后必须用自然语言整理最终解答，不要在最终回复中输出 function_calls、XML 或代码块形式的工具调用。
4. answer 的写法按题型区分：
   - 非证明题：answer 只放最终答案，不要放推导过程。例如“10”“牛顿第一定律”“\\(\\frac{\\sqrt{\\pi}}{2}\\)”。
   - 证明题：answer 放完整证明过程，证明应和 reasoning_process 一样使用自然、连贯、完整的推理步骤。
5. 公式、特殊符号和答案推荐使用 LaTeX 格式。
6. 如果题目包含歧义或超出课程范围，请在 reasoning_process 中说明；若完全无法解答，请说明原因。
7. 最终回复必须严格使用下面两行字段名，不要添加其它标题或说明：
reasoning_process: <自然语言做题过程>
answer: <最终答案；证明题为完整证明>
"""


class MathAgent:
    """解题智能体，通过调用 Kimi K2.5 + RAG 完成题目解答。"""

    def __init__(self,
                 rag_data_dir: Optional[str] = None,
                 subjects: Optional[List[str]] = AVAILABLE_SUBJECTS):
        self.client = OpenAI(
            api_key=KIMI_API_KEY,
            base_url=KIMI_BASE_URL,
            max_retries=0,
        )
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
            
        # 2. 从验证集、提交输入目录和 rag 知识库内部所有可能目录兜底寻找
        agent_dir = os.path.dirname(os.path.abspath(__file__))
        workspace_dir = os.path.dirname(agent_dir)
        project_dir = os.path.dirname(workspace_dir)
        search_dirs = [
            os.getcwd(),
            workspace_dir,
            os.path.join(workspace_dir, "val_data"),
            os.path.join(project_dir, "agent", "inputs"),
            self.rag_data_dir,
        ]
        for subj in self.subjects:
            search_dirs.append(os.path.join(self.rag_data_dir, subj))
            
        for d in search_dirs:
            candidate = os.path.join(d, raw_path)
            if os.path.exists(candidate):
                return candidate
            # 兼容数据里写成 images/foo.png，但实际搜索目录已经是 images 的情况
            basename_candidate = os.path.join(d, os.path.basename(raw_path))
            if os.path.exists(basename_candidate):
                return basename_candidate
        return None

    def _create_chat_completion(self, messages: List[Dict[str, Any]], use_tools: bool = True):
        kwargs = {
            "model": self.model,
            "messages": messages,
            "max_tokens": MAX_OUTPUT_TOKENS,
            "timeout": API_TIMEOUT_SECONDS,
        }
        if use_tools:
            kwargs["tools"] = TOOL_DEFINITION
            kwargs["tool_choice"] = "auto"
        return self.client.chat.completions.create(**kwargs)

    def _should_retry_without_tools(self, error: Exception) -> bool:
        """少数多模态模型不支持 image_url 与 tools 同传，遇到该类错误降级为纯视觉问答。"""
        message = str(error).lower()
        tool_terms = ("tool", "function", "tools", "tool_choice")
        image_terms = ("image", "vision", "multimodal", "image_url")
        return any(term in message for term in tool_terms) and any(term in message for term in image_terms)

    def _should_enable_tools(
        self,
        q_id: str,
        q_type: str,
        difficulty: str,
        question: str,
        has_image: bool = False,
    ) -> bool:
        """Decide whether the first model call should expose python_exec."""
        if has_image:
            return False

        qid = (q_id or "").upper()
        prefix = qid.split("_", 1)[0]
        text = f"{q_type}\n{difficulty}\n{question}"

        proof_like_terms = ("证明题", "构造题", "证明", "反证法", "说明矛盾", "解释")
        if any(term in text for term in proof_like_terms):
            return False

        calculus_terms = (
            "积分", "二重积分", "三重积分", "极限", "求导", "导数",
            "微分", "级数", "递推", "Beta", "Gamma", "保留到",
        )
        linear_algebra_terms = (
            "矩阵", "行列式", "det", "方程组", "通解", "特征值",
            "特征向量", "秩", "逆矩阵", "线性相关", "线性无关",
        )
        numeric_terms = (
            "计算", "求值", "数值", "近似", "保留", "解方程",
            "最大功率", "功率", "电流", "电压", "谐振", "传输参数",
        )

        if prefix == "CAL":
            return any(term in text for term in calculus_terms + numeric_terms)

        if prefix == "LA":
            return any(term in text for term in linear_algebra_terms + numeric_terms)

        if prefix == "CIR":
            return "计算题" in q_type or any(term in text for term in numeric_terms)

        explicit_python_need = any(term in text for term in ("用 Python", "python", "数值验证"))
        return explicit_python_need

    def _call_model_with_retry(
        self,
        q_id: str,
        messages: List[Dict[str, Any]],
        stage: str,
        use_tools: bool = True,
        allow_tool_fallback: bool = False,
    ) -> Optional[Any]:
        """统一封装 API 重试；图片+工具不兼容时只在首轮自动降级一次。"""
        for attempt in range(1, MAX_TOOL_RETRIES + 1):
            try:
                response = self._create_chat_completion(messages, use_tools=use_tools)
                self._log_response_state(q_id, response, stage)
                return response
            except Exception as e:
                if use_tools and allow_tool_fallback and self._should_retry_without_tools(e):
                    logger.warning(f"题目 {q_id} {stage} 工具与图片同传失败，降级为无工具调用: {e}")
                    return self._call_model_with_retry(
                        q_id,
                        messages,
                        f"{stage}/无工具降级",
                        use_tools=False,
                        allow_tool_fallback=False,
                    )
                wait_time = 2 ** attempt
                logger.warning(
                    f"题目 {q_id} {stage} API 调用失败 "
                    f"(尝试 {attempt}/{MAX_TOOL_RETRIES})，{wait_time}秒后重试: {e}"
                )
                time.sleep(wait_time)
        return None

    def _log_response_state(self, q_id: str, response: Any, stage: str) -> None:
        try:
            choice = response.choices[0]
            msg = choice.message
            tool_count = len(msg.tool_calls or [])
            content_len = len(msg.content or "")
            reasoning_content = getattr(msg, "reasoning_content", None)
            reasoning_len = len(reasoning_content or "")
            finish_reason = getattr(choice, "finish_reason", "")
            logger.info(
                f"题目 {q_id} {stage} 返回: finish_reason={finish_reason}, "
                f"content_len={content_len}, reasoning_len={reasoning_len}, tool_calls={tool_count}"
            )
        except Exception as e:
            logger.warning(f"题目 {q_id} 无法记录模型返回状态: {e}")

    def _assistant_message_to_dict(self, message: Any) -> Dict[str, Any]:
        """把 SDK 的 assistant message 转成可安全回传给 Chat Completions 的 dict。"""
        msg: Dict[str, Any] = {
            "role": "assistant",
            "content": message.content or "",
        }
        reasoning_content = getattr(message, "reasoning_content", None)
        if reasoning_content:
            msg["reasoning_content"] = reasoning_content
        if message.tool_calls:
            msg["tool_calls"] = [
                {
                    "id": tool_call.id,
                    "type": "function",
                    "function": {
                        "name": tool_call.function.name,
                        "arguments": tool_call.function.arguments or "{}",
                    },
                }
                for tool_call in message.tool_calls
            ]
        return msg

    def _extract_tool_code(self, raw_args: str) -> str:
        """兼容 JSON、Markdown JSON 块和少量 XML 风格残片。"""
        raw_args = (raw_args or "").strip()
        raw_args = re.sub(r'^```(?:json)?\s*', '', raw_args, flags=re.IGNORECASE)
        raw_args = re.sub(r'\s*```$', '', raw_args)
        try:
            parsed = json.loads(raw_args)
            if isinstance(parsed, dict):
                return str(parsed.get("code", ""))
        except Exception:
            pass

        code_match = re.search(
            r'<parameter\s+name=["\']code["\']>\s*(?P<code>[\s\S]*?)\s*</parameter>',
            raw_args,
            re.IGNORECASE,
        )
        if code_match:
            return code_match.group("code")

        # 最后兜底：如果模型直接把代码作为 arguments 返回，就原样执行。
        return raw_args

    def _execute_tool_calls(self, q_id: str, messages: List[Dict[str, Any]], assistant_message: Any) -> None:
        """执行并回填当前 assistant 消息中的所有工具调用，保证消息链闭合。"""
        tool_calls = assistant_message.tool_calls or []
        if not tool_calls:
            return

        logger.info(f"题目 {q_id} 执行工具调用数: {len(tool_calls)}")
        for tool_call in tool_calls:
            if tool_call.function.name != "python_exec":
                tool_response_content = "未知工具"
            else:
                try:
                    code = self._extract_tool_code(tool_call.function.arguments)
                    if not code.strip():
                        tool_response_content = "执行错误: python_exec 的 code 参数为空，请重新给出可执行代码。"
                    else:
                        stdout, stderr = run_python_code(code, timeout=CODE_EXEC_TIMEOUT)
                        if stderr:
                            tool_response_content = f"执行错误:\n{stderr}\n标准输出:\n{stdout}"
                        else:
                            tool_response_content = stdout if stdout else "执行成功（无输出）"
                except Exception as e:
                    tool_response_content = f"工具执行失败: {str(e)}"

            messages.append({
                "role": "tool",
                "content": tool_response_content,
                "tool_call_id": tool_call.id,
            })

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
                    logger.info(f"题目 {q_id} 已加载图片: {image_path} ({os.path.getsize(image_path)} bytes)")
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
        has_image = isinstance(user_content, list)
        use_tools = True
        logger.info(f"题目 {q_id} 开始调用模型，包含图片: {has_image}, 启用工具: {use_tools}")

        # 4. 初次 API 调用（带指数退避）
        response = self._call_model_with_retry(
            q_id,
            messages,
            "首轮",
            use_tools=use_tools,
            allow_tool_fallback=has_image,
        )
        if response is None:
            return self._fallback_solve(item)

        assistant_message = response.choices[0].message
        messages.append(self._assistant_message_to_dict(assistant_message))

        # 5. 工具调用循环
        max_turns = 3
        for turn_idx in range(max_turns):
            if not assistant_message.tool_calls:
                break

            logger.info(f"题目 {q_id} 第 {turn_idx + 1} 轮工具调用数: {len(assistant_message.tool_calls)}")
            self._execute_tool_calls(q_id, messages, assistant_message)

            response = self._call_model_with_retry(
                q_id,
                messages,
                f"工具后第 {turn_idx + 1} 轮",
                use_tools=True,
            )
            if response is None:
                return self._fallback_solve(item)

            assistant_message = response.choices[0].message
            messages.append(self._assistant_message_to_dict(assistant_message))

        # 6. 提取最终答案
        final_content = assistant_message.content or ""
        if assistant_message.tool_calls or not final_content.strip():
            if assistant_message.tool_calls:
                logger.warning(f"题目 {q_id} 仍有未收束工具调用，改用无工具收尾。")
                # Chat Completions 要求每个 assistant tool_call 后必须紧跟对应 tool 消息。
                # 达到轮数上限或模型同时返回正文与工具调用时，也先补齐工具响应，
                # 再发无工具收尾请求，避免 400 invalid_request_error，并确保解题链条完整。
                self._execute_tool_calls(q_id, messages, assistant_message)
            else:
                logger.warning(f"题目 {q_id} 模型返回正文为空，改用无工具重试收尾。")
            messages.append({
                "role": "user",
                "content": "请停止调用工具，直接基于已有题目信息和工具结果，严格按 reasoning_process 和 answer 两个字段给出最终解答。",
            })
            response = self._call_model_with_retry(q_id, messages, "无工具收尾", use_tools=False)
            if response is not None:
                assistant_message = response.choices[0].message
                final_content = assistant_message.content or ""
            else:
                logger.warning(f"题目 {q_id} 无工具收尾失败，保留已有正文。")

        if not final_content.strip():
            logger.warning(f"题目 {q_id} 最终正文仍为空，使用不带历史工具链的直接重试。")
            direct_messages = [
                {"role": "system", "content": system_prompt},
                {"role": "user", "content": user_content},
                {
                    "role": "user",
                    "content": "上一次返回为空。请不要调用工具，直接输出两行：reasoning_process: ... 和 answer: ...。",
                },
            ]
            response = self._call_model_with_retry(q_id, direct_messages, "空正文直接重试", use_tools=False)
            if response is not None:
                final_content = response.choices[0].message.content or ""

        if not final_content.strip():
            return {
                "question_id": q_id,
                "reasoning_process": "模型多次调用后仍返回空正文，未能生成可解析解答。请查看日志中的 finish_reason、content_len 和 tool_calls。",
                "answer": "[模型返回空内容]",
            }

        answer, reasoning = self._parse_final_output(final_content, q_type)
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
        ans = self._strip_function_call_markup(ans)
        ans = re.sub(r'^```(?:json|markdown|text)?\s*', '', ans, flags=re.IGNORECASE)
        ans = re.sub(r'\s*```$', '', ans)
        if ans.startswith("**") and ans.endswith("**"):
            ans = ans[2:-2].strip()
        ans = re.sub(r'\\boxed\{(.*)\}', r'\1', ans).strip()
        if re.fullmatch(r'</?function_calls>|</?invoke[^>]*>|</?parameter[^>]*>', ans, flags=re.IGNORECASE):
            return ""
        return ans

    def _strip_function_call_markup(self, text: str) -> str:
        """清理模型偶尔泄漏到正文里的伪工具调用标记。"""
        if not text:
            return ""
        text = re.sub(r'<function_calls>[\s\S]*?</function_calls>', '', text, flags=re.IGNORECASE)
        text = re.sub(r'<invoke\b[\s\S]*?</invoke>', '', text, flags=re.IGNORECASE)
        text = re.sub(r'</?function_calls>', '', text, flags=re.IGNORECASE)
        return text.strip()

    def _parse_final_output(self, content: str, q_type: str = "") -> Tuple[str, str]:
        content = self._strip_function_call_markup(content).strip()
        answer = ""
        reasoning = content

        json_match = re.search(r'\{[\s\S]*\}', content)
        if json_match:
            try:
                data = json.loads(json_match.group(0))
                if isinstance(data, dict):
                    reasoning = str(
                        data.get("reasoning_process")
                        or data.get("reasoning")
                        or data.get("思考过程")
                        or data.get("推理过程")
                        or ""
                    ).strip()
                    answer = str(data.get("answer") or data.get("答案") or "").strip()
                    if reasoning or answer:
                        return self._clean_answer(answer), reasoning
            except Exception:
                pass

        fenced_match = re.search(r'```(?:json|markdown|text)?\s*([\s\S]*?)\s*```', content, re.IGNORECASE)
        if fenced_match:
            inner_answer, inner_reasoning = self._parse_final_output(fenced_match.group(1), q_type)
            if inner_answer or inner_reasoning:
                return inner_answer, inner_reasoning

        field_match = re.search(
            r"^\s*(?:[-*]\s*)?reasoning_process\s*[：:]\s*(?P<reasoning>[\s\S]*?)\n\s*(?:[-*]\s*)?answer\s*[：:]\s*(?P<answer>[\s\S]*)\Z",
            content,
            re.IGNORECASE,
        )
        if field_match:
            reasoning = field_match.group("reasoning").strip()
            answer = self._clean_answer(field_match.group("answer"))
            return answer, reasoning

        loose_field_match = re.search(
            r"^\s*(?:[-*]\s*)?reasoning_process\s*[：:]\s*(?P<reasoning>[\s\S]*?)\s+answer\s*[：:]\s*(?P<answer>[\s\S]*)\Z",
            content,
            re.IGNORECASE,
        )
        if loose_field_match:
            reasoning = loose_field_match.group("reasoning").strip()
            answer = self._clean_answer(loose_field_match.group("answer"))
            return answer, reasoning

        cn_field_match = re.search(
            r"^\s*(?:[-*]\s*)?(?:推理过程|思考过程|reasoning)\s*[：:]\s*(?P<reasoning>[\s\S]*?)\n\s*(?:[-*]\s*)?(?:最终答案|答案|answer)\s*[：:]\s*(?P<answer>[\s\S]*)\Z",
            content,
            re.IGNORECASE,
        )
        if cn_field_match:
            reasoning = cn_field_match.group("reasoning").strip()
            answer = self._clean_answer(cn_field_match.group("answer"))
            return answer, reasoning

        heading_match = re.search(
            r"(?:^|\n)\s*#+\s*(?:推理过程|思考过程|reasoning_process|reasoning)\s*\n(?P<reasoning>[\s\S]*?)"
            r"(?:\n\s*#+\s*(?:最终答案|答案|answer)\s*\n(?P<answer>[\s\S]*))\Z",
            content,
            re.IGNORECASE,
        )
        if heading_match:
            reasoning = heading_match.group("reasoning").strip()
            answer = self._clean_answer(heading_match.group("answer") or "")
            return answer, reasoning

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
        if "证明" in str(q_type) and not answer:
            answer = content
        return answer, reasoning

    def _extract_answer_from_text(self, text: str) -> str:
        text = self._strip_function_call_markup(text)
        lines = [line.strip() for line in text.strip().split("\n") if line.strip()]
        if lines:
            for line in reversed(lines):
                cleaned = self._clean_answer(line)
                if not cleaned:
                    continue
                m = re.match(r"(?:答案|结果|因此|所以)[：:，,]?\s*(.*)", cleaned)
                if m and m.group(1).strip():
                    return self._clean_answer(m.group(1))
                if "=" in cleaned:
                    tail = cleaned.rsplit("=", 1)[-1].strip(" 。；;，,")
                    if 0 < len(tail) <= 80:
                        return self._clean_answer(tail)
                if not re.search(r'function_calls|invoke|parameter', cleaned, re.IGNORECASE):
                    return cleaned
        return "[未提取到答案]"

    def _fallback_solve(self, item: Dict[str, Any]) -> Dict[str, str]:
        return {
            "question_id": str(item.get("question_id", "")),
            "reasoning_process": "由于模型API临时不可用或运行超时，无法得出解答。",
            "answer": "[API 调用失败]",
        }
