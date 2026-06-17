import os
import logging

logging.getLogger("httpx").setLevel(logging.WARNING)
logging.getLogger("openai").setLevel(logging.WARNING)

# Kimi API 配置
KIMI_API_KEY = os.getenv('MOONSHOT_API_KEY')
KIMI_BASE_URL = "https://api.moonshot.cn/v1"
MODEL_NAME = "kimi-k2.5"

# 工具调用与执行
MAX_TOOL_RETRIES = 3
CODE_EXEC_TIMEOUT = 10  # 适当放宽，sympy 有时需要
API_TIMEOUT_SECONDS = int(os.getenv("KIMI_API_TIMEOUT", "60"))
MAX_OUTPUT_TOKENS = int(os.getenv("KIMI_MAX_OUTPUT_TOKENS", "4096"))

# RAG 知识库目录（优先使用环境变量，否则自动探测常见路径）
RAG_DATA_DIR = os.getenv("RAG_DATA_DIR", "rag")

# 需要加载的学科列表
AVAILABLE_SUBJECTS = [
    "calculus1", "calculus2", "electric1", "electric2",
    "electromagnetic", "linearalgebra", "optics", "quantum"
]
