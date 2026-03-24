# Basic-Courses-Agent
2026“未央城”智能体大赛

## 简要文件框架

```text
Basic-Courses-Agent/
├── data/                  # 原始数据与处理后的数据
│   ├── raw/               # 原始 PDF 教材、讲义
│   └── processed/         # 解析后的 Markdown/JSON
├── scripts/               # 数据处理脚本
│   └── build_knowledge.py # 向量库构建脚本
├── src/                   # 核心代码
│   ├── agents/            # Agent 逻辑
│   │   ├── react_agent.py # 核心 ReAct 逻辑实现
│   │   └── prompts.py     # 统一存放 Prompts
│   ├── tools/             # 工具集成
│   │   ├── retriever.py   # 数据库检索接口
│   │   └── calculator.py  # 符号计算/数值计算接口 (SymPy)
│   └── main.py            # 主程序入口
├── tests/                 # 测试用例 (课后习题等验证)
├── README.md              # 项目介绍和文件框架
└── requirements.txt       # 项目依赖