# 处理后数据说明

该目录保存从电子教材中抽取并格式化后的 JSON 文件。

- 数据已由 `scripts/extract.py` 从 `data/raw/` 的 PDF 电子教材中提取。
- `processed/` 中存储的是结构化、格式化的 JSON 文件，适合作为后续向量化和 FAISS 构建的输入。
- 此阶段不直接保存 FAISS 索引结果，向量库生成由 `scripts/build.py` 负责。

处理流程一般为：从 `data/raw/` 读取 PDF -> 运行 `scripts/extract.py` 提取结构化 JSON -> 输出到 `data/processed/`。