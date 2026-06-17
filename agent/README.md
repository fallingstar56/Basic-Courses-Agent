# 基础赛道解题智能体（含 RAG + 多模态）

## 功能
- 基于 **Kimi K2.5** 大模型，自动解答微积分、物理、电路、线性代数题目。
- **RAG 增强**：从 `src/rag` 下的学科目录中读取 `.md` 教材知识和 `.json` 例题思考过程，为模型提供上下文。
- **多模态能力**：支持题目中包含图片，自动编码为 base64 送入模型。
- 通过 **Function Calling** 动态执行 Python 代码，实现数值计算与符号推导。
- 完善的错误处理：API 失败重试、代码执行超时终止、输入校验等。

## 目录结构
src/
├── agent.py # 核心智能体
├── rag.py # RAG 检索模块
├── tool_executor.py # Python 代码执行器
├── config.py # API 密钥、路径、超时等配置
├── submission.json # 比赛入口声明
└── rag/ # 知识库根目录
├── calculus1/
│ ├── calculus1.md
│ ├── calculus1.json
│ └── merged_images/ # 教材/例题中的图片
├── electric1/
│ ├── *.md, *.json
│ └── merged_images/
└── ...
inputs/
└── images/ # 输入题目图片的默认搜索路径


## 使用方式
1. 安装依赖：
   ```bash
   pip install -r requirements.txt