# extract.py 文档说明

本文档详细说明 `scripts/extract.py` 中各个函数、类及其作用、输入输出和实现逻辑。

## 概览

`extract.py` 主要负责：

- 调用 zhipuAI 接口生成文本结果
- 识别文件中以“例X.X.X”形式标记的题目块
- 将题干与解答分离
- 根据“证明”或“解”判断题型
- 识别竖线+横线的结束标记，截断解答
- 调用 AI 判断题目难度
- 输出最终 JSON 列表


## 常量

- `DEFAULT_API_BASE`
  - 默认 zhipuAI API 接口地址
- `DEFAULT_MODEL`
  - 默认 zhipuAI 模型名称


## 类：ZhipuAIClient

### `__init__(self, api_key: str, model: str = DEFAULT_MODEL, api_base: str = DEFAULT_API_BASE) -> None`

- 作用：创建 zhipuAI 客户端实例
- 参数：
  - `api_key`：必填，zhipuAI 的 Bearer Token
  - `model`：可选，默认 `DEFAULT_MODEL`
  - `api_base`：可选，默认 `DEFAULT_API_BASE`
- 行为：
  - 校验 `api_key` 是否存在
  - 去掉 `api_key` 头尾空白
  - 规范化 `api_base` 末尾不包含 `/`

### `create_completion(self, content: str, temperature: float = 0.0, max_tokens: int = 2048, top_p: float = 1.0) -> str`

- 作用：调用 zhipuAI 的聊天补全接口，获取模型输出文本
- 参数：
  - `content`：要发送给模型的输入内容
  - `temperature`：生成温度
  - `max_tokens`：最大输出 token 数量
  - `top_p`：采样阈值
- 返回：模型输出文本字符串
- 实现：
  - 构造符合 zhipuAI chat/completions 的请求体
  - 调用 `_post_json`
  - 通过 `_extract_response_text` 提取文本

### `_post_json(self, url: str, payload: dict[str, Any], headers: dict[str, str]) -> dict[str, Any]`

- 作用：执行 HTTP POST 请求并解析 JSON 响应
- 参数：
  - `url`：请求地址
  - `payload`：JSON 字典
  - `headers`：HTTP 头
- 返回：解析后的 JSON 对象
- 实现：
  - 优先使用 `requests` 库
  - 如果没有 `requests`，回退到标准库 `urllib`
  - 抛出 HTTP 相关错误时包含响应正文

### `_extract_response_text(self, response: dict[str, Any]) -> str`

- 作用：从 zhipuAI 返回的 JSON 中提取文本结果
- 参数：
  - `response`：zhipuAI 的响应 JSON
- 返回：提取后的文本字符串
- 逻辑：
  - 优先检查 `choices[0].message.content`
  - 其次检查 `choices[0].text`
  - 再检查 `data[0].text`
  - 最后检查顶层 `text`
  - 如果都找不到则抛出异常


## 函数：is_end_marker_line(line: str) -> bool

- 作用：判断一行是否为“结束标记”行
- 参数：
  - `line`：输入文本行
- 返回：布尔值，表示是否为结束符号行
- 规则：
  - 去掉前后空白后为空则返回 `False`
  - 如果整行只包含空白、竖线 `|`、横线 `-` 或 Unicode 画线字符，且长度 >= 3，则认为是结束标记
  - 如果包含类似 `│─`、`┤━`、`─┘` 等组合，也认为是结束标记


## 函数：split_question_blocks(content: str) -> list[dict[str, Any]]

- 作用：将源文本拆分为题目块
- 参数：
  - `content`：整个 `.py` 文件文本内容
- 返回：题目块列表，每个块为字典，包含 `question_id` 和 `lines`
- 规则：
  - 使用正则 `例\s*(\d+(?:\.\d+)*)` 匹配题号
  - 每出现一个新的题号时开启新块
  - 当前块结束后保存到列表
  - 每个块保留从题号那一行开始的所有后续行


## 函数：split_question_answer(block: dict[str, Any]) -> dict[str, str]

- 作用：将单个题目块拆分为题干和解答
- 参数：
  - `block`：由 `split_question_blocks` 生成的单个块，包含 `question_id` 和 `lines`
- 返回：
  - `question_id`：题号
  - `type`：题目类型，`数值计算` 或 `推导题`
  - `question`：题干文本
  - `answer`：解答文本
- 规则：
  - 将 `block['lines']` 拼接成完整文本
  - 查找首个以 `证明` 或 `解` 开头的行
  - 若未找到，则整个内容作题干，`answer` 置空，`type` 默认为 `数值计算`
  - 找到后：
    - 题干为 `answer_start` 之前内容
    - 解答为 `answer_start` 之后内容
  - 对解答部分逐行检测结束标记行，遇到后截断
  - 解答前缀为 `证明` 时 `type=推导题`
  - 解答前缀为 `解` 时 `type=数值计算`
  - 默认 `type=数值计算`


## 函数：infer_difficulty(client: ZhipuAIClient, question_text: str) -> str

- 作用：调用 zhipuAI 判断题目难度
- 参数：
  - `client`：已初始化的 `ZhipuAIClient`
  - `question_text`：题干文本
- 返回：AI 预测的难度标签
- 实现：
  - 构造简短提示，要求仅返回“简单、中等、较难、困难”之一
  - 调用 `client.create_completion`
  - 取返回结果第一行作为难度标签
  - 若返回为空，则默认返回 `中等`


## 函数：extract_questions_from_text(content: str, client: ZhipuAIClient) -> list[dict[str, str]]

- 作用：从完整文本中提取题目信息列表
- 参数：
  - `content`：整个 `.py` 文件文本
  - `client`：`ZhipuAIClient` 实例
- 返回：题目对象列表
- 逻辑：
  - 先调用 `split_question_blocks` 拆分题目块
  - 对每个块调用 `split_question_answer` 得到题干/解答/类型
  - 对每个题干调用 `infer_difficulty` 得到难度
  - 组合成最终字典并返回


## 函数：process_high_calculus_py(input_path: Path, api_key: str, model: str = DEFAULT_MODEL, temperature: float = 0.0) -> str

- 作用：处理单个高等微积分 `.py` 文件，并返回最终 JSON
- 参数：
  - `input_path`：待处理文件路径
  - `api_key`：zhipuAI API Key
  - `model`：zhipuAI 模型名称
  - `temperature`：调用模型时的温度参数
- 返回：
  - JSON 字符串，格式化输出题目列表
- 实现：
  - 校验文件存在且后缀为 `.py`
  - 读取文件全文
  - 初始化 `ZhipuAIClient`
  - 调用 `extract_questions_from_text`
  - 将结果 JSON 序列化为 `ensure_ascii=False` 的字符串


## 函数：parse_args() -> argparse.Namespace

- 作用：解析脚本命令行参数
- 参数：无
- 返回：解析后的命令行参数对象
- 支持参数：
  - `--api-key`：zhipuAI API Key
  - `--model`：模型名称，默认 `DEFAULT_MODEL`
  - `--input`：输入 `.py` 文件路径，默认 `data/raw/高等微积分1.py`
  - `--temperature`：生成温度，默认 `0.0`


## 函数：main() -> int

- 作用：脚本入口函数
- 参数：无
- 返回：退出码
- 逻辑：
  - 解析命令行参数
  - 从 `--api-key` 或环境变量 `ZHIPU_API_KEY` 获取 API Key
  - 如果缺少 Key，则打印错误并返回 `1`
  - 调用 `process_high_calculus_py`
  - 打印处理结果并返回 `0`
  - 发生异常时打印错误并返回 `2`


## 运行方式

```bash
python scripts/extract.py --api-key YOUR_API_KEY
```

如果你希望，我也可以继续补充一份更简洁的函数调用示例。