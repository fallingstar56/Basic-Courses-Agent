"""基于 TF‑IDF 的教材知识与习题检索器，支持中英文混排。"""
import os
import json
import re
import logging
from typing import List, Tuple, Optional

from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.metrics.pairwise import cosine_similarity

logger = logging.getLogger(__name__)


def _zh_en_tokenizer(text: str) -> List[str]:
    """将中文按单字切分，英文/数字按连续片段切分，简单高效。"""
    tokens = re.findall(r'[\u4e00-\u9fff]|[a-zA-Z0-9]+', text)
    return tokens


class RAGRetriever:
    def __init__(self, rag_data_dir: str, subjects: Optional[List[str]] = None):
        self.rag_data_dir = rag_data_dir
        self.knowledge_docs: List[str] = []
        self.example_questions: List[str] = []
        self.example_details: List[dict] = []

        if subjects is None:
            subjects = self._scan_subjects()
        if not subjects:
            # 不抛出异常，让程序优雅降级（RAG 返回空结果）
            logger.warning(f"未找到任何学科目录，RAG 将返回空结果。")
        else:
            for subj in subjects:
                subj_path = os.path.join(rag_data_dir, subj)
                if not os.path.isdir(subj_path):
                    logger.warning(f"学科目录不存在，跳过：{subj_path}")
                    continue
                self._load_md_files(subj_path)
                self._load_json_files(subj_path)

        logger.info(f"已加载 {len(self.knowledge_docs)} 条知识文档，{len(self.example_details)} 个例题。")

        # 使用自定义分词器构建 TF‑IDF 索引
        self.know_vectorizer = TfidfVectorizer(
            max_features=5000,
            tokenizer=_zh_en_tokenizer,
            analyzer='word',
            lowercase=False
        )
        self.exam_vectorizer = TfidfVectorizer(
            max_features=5000,
            tokenizer=_zh_en_tokenizer,
            analyzer='word',
            lowercase=False
        )

        self.know_tfidf = None
        if self.knowledge_docs:
            self.know_tfidf = self.know_vectorizer.fit_transform(self.knowledge_docs)

        self.exam_tfidf = None
        if self.example_questions:
            self.exam_tfidf = self.exam_vectorizer.fit_transform(self.example_questions)

    # 其余方法保持不变...
    def _scan_subjects(self) -> List[str]:
        try:
            return [d for d in os.listdir(self.rag_data_dir)
                    if os.path.isdir(os.path.join(self.rag_data_dir, d))]
        except FileNotFoundError:
            return []

    def _load_md_files(self, subj_path: str):
        for fname in os.listdir(subj_path):
            if fname.lower().endswith('.md'):
                path = os.path.join(subj_path, fname)
                try:
                    with open(path, 'r', encoding='utf-8') as f:
                        content = f.read()
                    if content.strip():
                        self.knowledge_docs.append(content)
                except Exception as e:
                    logger.warning(f"读取 {path} 失败: {e}")

    def _load_json_files(self, subj_path: str):
        for fname in os.listdir(subj_path):
            if fname.lower().endswith('.json'):
                path = os.path.join(subj_path, fname)
                try:
                    with open(path, 'r', encoding='utf-8') as f:
                        data = json.load(f)
                    if isinstance(data, list):
                        for item in data:
                            q = item.get('question', '')
                            if q:
                                self.example_questions.append(q)
                                self.example_details.append(item)
                except Exception as e:
                    logger.warning(f"读取 {path} 失败: {e}")

    def retrieve(self, query: str,
                 know_top_k: int = 2,
                 exam_top_k: int = 2) -> Tuple[List[str], List[Tuple[dict, float]]]:
        know_texts = []
        examples = []

        if self.know_tfidf is not None:
            query_vec = self.know_vectorizer.transform([query])
            sims = cosine_similarity(query_vec, self.know_tfidf).flatten()
            top_indices = sims.argsort()[::-1][:know_top_k]
            for idx in top_indices:
                if sims[idx] > 0:
                    know_texts.append(self.knowledge_docs[idx])

        if self.exam_tfidf is not None:
            query_vec = self.exam_vectorizer.transform([query])
            sims = cosine_similarity(query_vec, self.exam_tfidf).flatten()
            top_indices = sims.argsort()[::-1][:exam_top_k]
            for idx in top_indices:
                if sims[idx] > 0:
                    examples.append((self.example_details[idx], float(sims[idx])))

        return know_texts, examples