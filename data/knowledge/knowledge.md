# 知识库数据说明

该目录保存由 FAISS 处理后的知识库数据。

- `knowledge/` 中存放 `scripts/build.py` 处理 `data/processed/` 后生成的结果。
- 典型产物是 `cong.json`，其中包含 FAISS 向量索引所需的结构化数据和检索结果信息。
- 该目录的数据可直接用于语义检索、问答和 Agent 调用。

处理流程一般为：从 `data/processed/` 读取格式化 JSON -> 运行 `scripts/build.py` 构建 FAISS 知识库 -> 输出到 `data/knowledge/cong.json`。