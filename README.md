# Basic-Courses-Agent
2026 “未央城” 智能体大赛 

本目录是参赛 Agent 的提交文件夹。评测时请保持目录结构不变，评测脚本会读取 `submission.json` 中声明的入口类和入口方法，动态加载 `agent.py` 中的 `MathAgent.solve(item)` 完成逐题测试。

## 目录结构

```text
agent/
├── agent.py            # Agent 主入口，包含 MathAgent 类
├── config.py           # 模型、超时、RAG 学科等配置
├── rag.py              # RAG 检索模块
├── tool_executor.py    # Python 代码执行工具
├── submission.json     # 评测入口声明
├── requirements.txt    # Python 依赖
└── rag/                # 随提交携带的知识库与例题材料
```

`submission.json` 当前配置如下：

```json
{
  "entry_class": "MathAgent",
  "entry_method": "solve",
  "python_version": "3.12"
}
```

## 环境要求

- Python 3.12，兼容 Python 3.10 及以上版本。
- 可访问 Moonshot/Kimi API。
- 需要设置环境变量 `MOONSHOT_API_KEY`，作为 Kimi API Key。

依赖安装命令：

```bash
pip install -r requirements.txt
```

如评测环境未预装 `pip`、虚拟环境或构建工具，请先按评测机标准流程准备 Python 环境。

## 在提交文件夹下安装依赖

进入提交文件夹：

```bash
cd agent
```

安装依赖：

```bash
pip install -r requirements.txt
```

设置 API Key：

```bash
# Linux / macOS
export MOONSHOT_API_KEY="your_api_key"

# Windows PowerShell
$env:MOONSHOT_API_KEY="your_api_key"
```

可选环境变量：

```bash
# API 请求超时时间，默认 60 秒
export KIMI_API_TIMEOUT=60

# 单次模型输出 token 上限，默认 4096
export KIMI_MAX_OUTPUT_TOKENS=4096
```

Windows PowerShell 下对应写法为：

```powershell
$env:KIMI_API_TIMEOUT="60"
$env:KIMI_MAX_OUTPUT_TOKENS="4096"
```

## 运行评测

若赛方使用本仓库提供的本地评测脚本，请保证提交目录位于 `workspace/agent/`，验证集位于 `workspace/val_data/`，然后从 `workspace` 目录执行：

```bash
cd ..
python evaluate.py
```

如果当前工作目录已经是仓库根目录，也可以直接执行：

```bash
python workspace/evaluate.py
```

评测脚本会自动完成以下流程：

1. 读取 `workspace/agent/submission.json`。
2. 将 `workspace/agent` 加入 Python 导入路径。
3. 导入 `agent.py`，实例化 `MathAgent`。
4. 对 `workspace/val_data/` 下的所有 JSON 题目逐题调用 `MathAgent.solve(item)`。
5. 将结果保存到 `workspace/evaluation_results.json`。

## 输入与输出约定

`solve(item)` 接收单题字典，题目字段由评测数据提供。Agent 会尽量读取以下常见字段：

- `question_id`：题目编号。
- `question`：题干文本。
- `type` / `question_type`：题型。
- `difficulty`：难度。
- `images` / `image` / `image_path`：图片路径。

`solve(item)` 返回字典，至少包含：

```json
{
  "reasoning_process": "解题过程",
  "answer": "最终答案"
}
```

其中 `answer` 只放最终答案；证明题则可放完整证明。

## 图片与 RAG 文件

- 题目图片会优先按评测脚本当前工作目录、`workspace/val_data/`、提交目录相关路径进行查找。
- `rag/` 目录必须与 `agent.py` 放在同一提交目录下，不需要额外设置 `RAG_DATA_DIR`。
- 请勿在评测前删除或移动 `rag/` 目录，否则知识库增强会失效。

## 常见问题

如果出现 `加载 Agent 失败`，请检查：

- 当前目录结构是否为 `workspace/agent/agent.py`。
- `submission.json` 是否存在且 JSON 格式正确。
- 是否已安装 `requirements.txt` 中的依赖。

如果出现 API 调用失败，请检查：

- `MOONSHOT_API_KEY` 是否已设置。
- 评测机网络是否允许访问 `https://api.moonshot.cn/v1`。
- API Key 是否有可用额度。

如果出现图片读取失败，请检查：

- 验证集中的图片相对路径是否能从 `workspace/val_data/` 或当前运行目录解析。
- 图片文件是否随验证集一起放置，例如 `workspace/val_data/images/xxx.png`。
