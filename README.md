# Basic-Courses-Agent
2026 “未央城” 智能体大赛 

## 目录结构
```text
Basic-Courses-Agent/
├── data/
│   ├── raw/               # 原始教材、资料 PDF 等原始数据
│   └── processed/         # 由脚本解析后的 Markdown/JSON 等知识文件
├── scripts/
│   └── build_knowledge.py # 用于构建向量数据库、嵌入等预处理脚本
├── src/
|   ├── prompts.py         # 提示语（Prompt）模板定义
│   └── main.py            # 程序入口（包含Agent逻辑）
├── tests/                 # 单元测试、集成测试、习题验证
├── README.md              # 项目说明文档
└── requirements.txt       # Python 依赖列表（当前为空或待补充）
```

## 安装与运行
1. 创建 Python 虚拟环境（推荐）
   ```bash
   python -m venv .venv
   source .venv/bin/activate   # macOS/Linux
   .venv\\Scripts\\activate  # Windows
   ```
2. 安装依赖（如果 `requirements.txt` 未空，请补充所需依赖）
   ```bash
   pip install -r requirements.txt
   # 可能需要以下依赖：
   # pip install openai langchain faiss-cpu numpy sympy
   ```
3. 运行主程序
   ```bash
   python src/main.py
   ```

## 数据处理流程
1. 将原始教材/讲义文件放入 `data/raw/`
2. 运行 `scripts/build_knowledge.py` 生成 `data/processed/` 中的知识文件
3. 启动 `src/main.py`，开始解决题目（包含reAct Agent逻辑）

## 贡献指南
- 阅读并补全 `requirements.txt` 中依赖
- 增加测试用例到 `tests/`