# Basic-Courses-Agent
2026 “未央城” 智能体大赛 

## 目录结构
```text
Basic-Courses-Agent/
├── data/
│   ├── raw/               # 最初未处理的 PDF 电子教材
│   ├── processed/         # 运行 scripts/extract.py 从 raw 中电子教材提取出的格式化 JSON 文件
│   └── knowledge/         # 运行 scripts/build.py 后，用 FAISS 处理生成的 cong.json 数据
├── scripts/
│   ├── extract.py         # 从 data/raw/ 的 PDF 提取结构化/格式化 JSON
│   └── build.py           # 使用 data/processed/ 中的 JSON，构建 FAISS 向量知识库，生成 data/knowledge/cong.json
├── src/
│   ├── prompts.py         # 提示语（Prompt）模板定义
│   └── main.py            # 程序入口（包含 Agent 逻辑）
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
1. 将原始教材/电子教材 PDF 文件放入 `data/raw/`
2. 运行 `python scripts/extract.py`，从 `data/raw/` 中提取格式化 JSON 到 `data/processed/`
3. 运行 `python scripts/build.py`，使用 FAISS 处理 `data/processed/`，生成 `data/knowledge/cong.json`
4. 启动 `python src/main.py`，开始解决题目（包含 Agent 逻辑）
