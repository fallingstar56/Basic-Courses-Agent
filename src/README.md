# 基础赛道解题智能体

## 功能
- 基于 Kimi K2.5 大模型，自动解答微积分（及物理、电路、线性代数）题目。
- 支持**数值计算、符号推导、证明题**等多种题型。
- 通过 Function Calling 动态执行 Python 代码，实现计算与验证。
- 完善的错误处理：API 调用失败时降级到 Baseline，工具执行超时自动终止。
- 输入校验与异常输入提示。

## 使用方式
1. 安装依赖：`pip install -r requirements.txt`
2. 设置环境变量 `KIMI_API_KEY` 为你的 Kimi API 密钥。
3. 实例化 `MathAgent`，调用 `solve(dict)` 即可。

## 文件说明
- `agent.py`：核心 Agent，负责与 LLM 交互，管理工具调用。
- `tool_executor.py`：安全执行 Python 代码的沙箱。
- `config.py`：配置信息。
- `submission.json`：比赛要求的入口声明。

## 注意事项
- 当前不处理 `image` 字段，若题目包含图片，模型仅根据文字部分作答。
- 代码执行超时默认为 5 秒，可在 `config.py` 中调整。
- 如遇完全未知的题型或超纲内容，模型会在推理中说明局限性。