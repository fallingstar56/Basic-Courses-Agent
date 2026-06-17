"""基于 TF-IDF 的示例检索器，用于 RAG。"""

import json
import re
import logging
from typing import List, Tuple

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

logger = logging.getLogger(__name__)

class ExampleRetriever:
    def __init__(self, json_path: str):
        """
        json_path: combined_result_examples.json 的路径
        """
        with open(json_path, 'r', encoding='utf-8') as f:
            self.examples = json.load(f)
        if not self.examples:
            raise ValueError("示例库为空！")

        # 仅保留 question 和 answer 用于检索
        self.texts = [ex['question'] for ex in self.examples]
        self.vectorizer = TfidfVectorizer(
            max_features=5000,
            stop_words=None,         # 保留数学符号，可自行添加停用词
            token_pattern=r'(?u)\b\w+\b'   # 简单的单词切分
        )
        self.tfidf_matrix = self.vectorizer.fit_transform(self.texts)
        logger.info(f"已构建 RAG 索引，共 {len(self.texts)} 条示例。")

    def retrieve(self, query: str, top_k: int = 3) -> List[Tuple[dict, float]]:
        """
        检索与 query 最相似的 top_k 个示例，返回 (示例字典, 相似度) 列表。
        """
        query_vec = self.vectorizer.transform([query])
        similarities = cosine_similarity(query_vec, self.tfidf_matrix).flatten()
        # 按相似度降序排序，取前 top_k
        top_indices = similarities.argsort()[::-1][:top_k]
        results = []
        for idx in top_indices:
            if similarities[idx] > 0:  # 只返回有正相似度的结果
                results.append((self.examples[idx], similarities[idx]))
        return results