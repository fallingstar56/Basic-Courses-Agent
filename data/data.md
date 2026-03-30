# 数据目录说明

此目录用于存放项目所需的数据文件。

- `raw/`：存放最初未处理的 `.pdf` 电子教材，作为 `scripts/extract.py` 的输入。
- `processed/`：存放 `scripts/extract.py` 从 `raw/` 提取出的结构化、格式化 JSON 文件，作为后续构建 FAISS 的输入。
- `knowledge/`：存放 `scripts/build.py` 使用 FAISS 处理 `processed/` 后生成的结果文件，例如 `cong.json`。

当前项目采用的流程是：
  1. 将原始 PDF 放入 `data/raw/`
  2. 运行 `scripts/extract.py` 提取 JSON 到 `data/processed/`
  3. 运行 `scripts/build.py` 构建 FAISS 知识库，输出到 `data/knowledge/`
  4. 运行 `src/main.py` 进行问答或检索

## 数据处理分工

1.基础物理+线性代数 尤梓萌

2.电路原理+微积分 许瀚元