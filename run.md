# Agent 当前完整运行流程

本文档记录当前仓库中实际用于本地评测的 Agent 运行方式和内部调用链。当前应重点看 `workspace/agent/` 这一套实现，而不是早期的 `src/` 版本。

## 1. 本地评测运行命令

推荐从仓库根目录开始执行：

```powershell
cd "d:\大一春季学期\Basic-Courses-Agent"
pip install -r .\workspace\agent\requirements.txt
$env:MOONSHOT_API_KEY="你的 Kimi API Key"
cd .\workspace
python .\evaluate.py
```

必须在 `workspace` 目录下运行 `python .\evaluate.py`，因为 `workspace/evaluate.py` 中的路径是相对当前工作目录写死的：

```python
VAL_DATA_DIR = "val_data"
AGENT_DIR = "agent"
SUBMISSION_FILE = os.path.join(AGENT_DIR, "submission.json")
OUTPUT_RESULT_FILE = "evaluation_results.json"
```

因此实际读取路径是：

```text
workspace/val_data/
workspace/agent/
workspace/agent/submission.json
```

评测完成后，结果会保存到：

```text
workspace/evaluation_results.json
```

## 2. 本地评测脚本流程

入口文件是：

```text
workspace/evaluate.py
```

执行 `python .\evaluate.py` 后，流程如下：

1. 将 `workspace/agent` 加入 Python 模块搜索路径：

   ```python
   sys.path.insert(0, os.path.abspath(AGENT_DIR))
   ```

2. 读取 `workspace/agent/submission.json`：

   ```json
   {
     "Team_name": "YourTeamName",
     "python_version": "3.12",
     "entry_class": "MathAgent",
     "entry_method": "solve"
   }
   ```

3. 动态导入 `agent.py`：

   ```python
   module = importlib.import_module("agent")
   ```

4. 根据 `submission.json` 实例化 Agent：

   ```python
   agent_instance = getattr(module, "MathAgent")()
   solve_method = getattr(agent_instance, "solve")
   ```

5. 遍历 `workspace/val_data/` 下所有 `.json` 文件。

6. 对每个 JSON 文件尝试多种编码读取：

   ```python
   ['utf-8', 'utf-16', 'gbk', 'utf-8-sig', 'utf-16le']
   ```

7. 如果文件内容是 `list`，则把题目加入总题目列表。

8. 逐题调用：

   ```python
   response = solve_method(item)
   ```

9. 打印每题的耗时、推理过程、模型答案、标准答案。

10. 将所有结果写入 `workspace/evaluation_results.json`。

## 3. Agent 初始化流程

核心 Agent 文件是：

```text
workspace/agent/agent.py
```

评测脚本实例化：

```python
MathAgent()
```

初始化时执行：

1. 创建 Kimi/OpenAI 兼容客户端：

   ```python
   self.client = OpenAI(api_key=KIMI_API_KEY, base_url=KIMI_BASE_URL)
   self.model = MODEL_NAME
   ```

2. `KIMI_API_KEY` 来自环境变量：

   ```python
   MOONSHOT_API_KEY
   ```

3. 如果没有显式传入 `rag_data_dir`，自动定位到当前 Agent 目录下的 RAG 文件夹：

   ```python
   current_dir = os.path.dirname(os.path.abspath(__file__))
   rag_data_dir = os.path.join(current_dir, "rag")
   ```

4. 默认加载 `config.py` 中的所有学科：

   ```python
   AVAILABLE_SUBJECTS = [
       "calculus1", "calculus2", "electric1", "electric2",
       "electromagnetic", "linearalgebra", "optics", "quantum"
   ]
   ```

5. 初始化 RAG 检索器：

   ```python
   self.retriever = RAGRetriever(self.rag_data_dir, self.subjects)
   ```

## 4. RAG 加载流程

RAG 代码在：

```text
workspace/agent/rag.py
```

`RAGRetriever` 初始化时会遍历 `workspace/agent/rag/` 下的学科目录，例如：

```text
workspace/agent/rag/calculus1/
workspace/agent/rag/electric1/
workspace/agent/rag/linearalgebra/
...
```

每个学科目录中：

- `.md` 文件会被加载为教材知识文档。
- `.json` 文件会被加载为例题库。

内部维护三组核心数据：

```python
self.knowledge_docs      # 教材/讲义文本
self.example_questions  # 例题题面文本，用于检索
self.example_details    # 例题完整 dict，用于拼入 prompt
```

然后分别构建两个 TF-IDF 索引：

```python
self.know_tfidf = self.know_vectorizer.fit_transform(self.knowledge_docs)
self.exam_tfidf = self.exam_vectorizer.fit_transform(self.example_questions)
```

检索时：

```python
know_texts, examples = self.retriever.retrieve(query, know_top_k=2, exam_top_k=2)
```

会返回：

- 最相关的 2 个教材知识片段。
- 最相关的 2 个例题。

注意：当前实现是“所有学科统一检索”，不是先判断学科再检索。

## 5. 单题 solve(item) 流程

每道题都会进入：

```python
MathAgent.solve(item)
```

输入 `item` 通常来自 `workspace/val_data/*.json`，字段包括：

```json
{
  "question_id": "...",
  "type": "...",
  "difficulty": "...",
  "question": "...",
  "answer": "..."
}
```

如果有图片，还可能包含：

```json
{
  "image": "..."
}
```

`solve(item)` 内部流程：

1. 读取题目信息：

   ```python
   q_id = str(item.get("question_id", ""))
   q_type = item.get("type", "未知类型")
   difficulty = item.get("difficulty", "未知难度")
   question = item.get("question", "").strip()
   image_raw = item.get("image")
   ```

2. 如果 `image` 字段为空，尝试从题目 HTML 中提取 `<img src="...">`。

3. 如果题目文本为空，直接返回空题错误。

4. 调用 RAG 构建系统提示词：

   ```python
   system_prompt = self._build_system_prompt(question, q_type)
   ```

5. 如果有图片，尝试解析图片路径并 base64 编码，作为多模态输入传给模型。

6. 构造 messages：

   ```python
   messages = [
       {"role": "system", "content": system_prompt},
       {"role": "user", "content": user_content},
   ]
   ```

7. 调用 Kimi 模型，并提供工具定义：

   ```python
   response = self.client.chat.completions.create(
       model=self.model,
       messages=messages,
       tools=TOOL_DEFINITION,
       tool_choice="auto",
   )
   ```

## 6. Prompt 构建流程

`_build_system_prompt(query, q_type)` 会先从 RAG 中检索：

```python
know_texts, examples = self.retriever.retrieve(query, know_top_k=2, exam_top_k=2)
```

然后从基础系统提示开始：

```python
BASE_SYSTEM_PROMPT
```

基础提示要求模型：

- 扮演清华大学理工科基础课程解题助手。
- 对题目逐步推理。
- 必要时调用 `python_exec` 工具。
- 最终输出简洁明确的 answer。

如果检索到教材知识，会追加：

```text
## 相关知识（来自教材/讲义）
[知识 1]:
...
[知识 2]:
...
```

如果检索到例题，会追加：

```text
## 参考示例（来自习题库）
[示例 1] (相似度: ...)
题目: ...
思考过程: ...
答案: ...
```

最终这个 prompt 会作为 `system` 消息送入模型。

## 7. ReAct / 工具调用流程

当前 Agent 的 ReAct 不是手写 `Thought/Action/Observation` 文本格式，而是用 Kimi/OpenAI 兼容的 Function Calling 实现。

工具定义在 `workspace/agent/agent.py`：

```python
TOOL_DEFINITION = [
    {
        "type": "function",
        "function": {
            "name": "python_exec",
            "description": "执行 Python 代码，用于数学计算、符号推导、数值验证等。",
            "parameters": {
                "type": "object",
                "properties": {
                    "code": {"type": "string"}
                },
                "required": ["code"],
            },
        },
    }
]
```

模型如果认为需要计算，会返回 `tool_calls`。Agent 随后进入最多 5 轮的工具调用循环：

```python
max_turns = 5
for _ in range(max_turns):
    if not assistant_message.tool_calls:
        break
    ...
```

每轮逻辑：

1. 检查模型是否请求工具调用。

2. 如果工具名不是 `python_exec`，返回“未知工具”。

3. 如果工具名是 `python_exec`，解析参数：

   ```python
   raw_args = tool_call.function.arguments
   code = json.loads(raw_args).get("code", "")
   ```

4. 调用本地 Python 执行器：

   ```python
   stdout, stderr = run_python_code(code, timeout=CODE_EXEC_TIMEOUT)
   ```

5. 将执行结果封装为 `role="tool"` 的消息：

   ```python
   tool_response = {
       "role": "tool",
       "content": tool_response_content,
       "tool_call_id": tool_call.id,
   }
   messages.append(tool_response)
   ```

6. 再次调用模型，让模型读取工具输出并继续推理：

   ```python
   response = self.client.chat.completions.create(
       model=self.model,
       messages=messages,
       tools=TOOL_DEFINITION,
       tool_choice="auto",
   )
   ```

对应的抽象流程是：

```text
模型推理
  -> 判断需要计算
  -> 调用 python_exec
  -> 本地执行 Python
  -> 工具结果回传给模型
  -> 模型继续推理
  -> 没有新的 tool_calls 后输出最终答案
```

## 8. Python 工具执行流程

工具执行代码在：

```text
workspace/agent/tool_executor.py
```

核心函数是：

```python
run_python_code(code: str, timeout: int = 5)
```

执行方式：

1. 使用 `multiprocessing.Process` 开子进程执行代码。

2. 限制可用 builtins，只开放常见安全函数，例如：

   ```python
   print, abs, min, max, pow, round, len, range,
   int, float, str, list, tuple, dict, set, bool,
   sum, sorted, enumerate, zip
   ```

3. 提供 `math` 常用函数。

4. 尝试提供 `sympy`，用于符号计算。

5. 重定向 stdout/stderr，捕获 `print()` 输出和异常栈。

6. 如果超过 `CODE_EXEC_TIMEOUT`，强制终止子进程。

返回值是：

```python
(stdout, stderr)
```

## 9. 最终答案解析

模型停止工具调用后，Agent 取最后一轮模型输出：

```python
final_content = assistant_message.content or ""
```

然后调用：

```python
answer, reasoning = self._parse_final_output(final_content)
```

解析规则主要匹配：

```python
r"(?:最终\s*)?答案\s*[：:]\s*(.+?)$"
r"(?:最终\s*)?结果\s*[：:]\s*(.+?)$"
r"\\boxed\{(.+?)\}"
```

如果没有解析到答案，则退化为取最后一行：

```python
answer = self._extract_answer_from_text(reasoning)
```

最终返回给评测脚本：

```python
{
    "question_id": q_id,
    "reasoning_process": reasoning.strip()[:2000],
    "answer": str(answer).strip(),
}
```

## 10. 总体链路图

```text
PowerShell
  -> cd workspace
  -> python evaluate.py
      -> 读取 agent/submission.json
      -> 导入 agent.py
      -> 实例化 MathAgent
          -> 读取环境变量 MOONSHOT_API_KEY
          -> 初始化 Kimi 客户端
          -> 定位 agent/rag
          -> 加载多学科 RAG
          -> 构建 TF-IDF 索引
      -> 读取 val_data/*.json
      -> 对每道题调用 MathAgent.solve(item)
          -> 校验题目字段
          -> 解析图片路径
          -> RAG 检索教材知识和例题
          -> 构造 system/user messages
          -> 第一次调用 Kimi
          -> 如有 tool_calls:
              -> 解析 python_exec 参数
              -> 本地执行 Python/sympy
              -> 将 stdout/stderr 作为 tool 消息回传
              -> 再次调用 Kimi
              -> 最多循环 5 轮
          -> 解析最终 answer 和 reasoning_process
      -> 打印每题结果
      -> 写入 evaluation_results.json
```

## 11. 重要注意事项

- 当前本地评测脚本必须从 `workspace` 目录运行。
- API Key 必须设置在环境变量 `MOONSHOT_API_KEY` 中。
- 当前 RAG 是所有学科统一检索，没有显式学科路由。
- `workspace/agent/README.md` 中部分描述仍写着 `src/rag`，但当前实际代码使用的是 `workspace/agent/rag`。
- 如果某个验证集 JSON 不是 list，`evaluate.py` 会跳过它。
- 如果模型 API 调用失败超过重试次数，Agent 会返回 `[API 调用失败]`。
