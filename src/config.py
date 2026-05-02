import os

KIMI_API_KEY = os.getenv('MOONSHOT_API_KEY')
KIMI_BASE_URL = "https://api.moonshot.cn/v1"
MODEL_NAME = "kimi-k2.5"         # Kimi K2.5 模型名，请以官方文档为准
MAX_TOOL_RETRIES = 3                         # 工具调用失败最大重试次数
CODE_EXEC_TIMEOUT = 5                        # Python 代码执行超时(秒)