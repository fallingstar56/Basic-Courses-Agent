import json
import os
import sys
import time

sys.path.insert(0, os.path.join(os.path.dirname(__file__), 'src'))
from agent import MathAgent


def load_json_multiencoding(path: str):
    """尝试多种常见编码读取 JSON 文件，返回解析后的对象。"""
    encodings = ['utf-8', 'utf-16-le', 'utf-16-be', 'utf-16', 'gbk', 'gb2312']
    for enc in encodings:
        try:
            with open(path, 'r', encoding=enc) as f:
                return json.load(f)
        except (UnicodeDecodeError, json.JSONDecodeError):
            continue
    raise ValueError(f"无法以任何尝试的编码读取文件: {path}")


def main():
    agent = MathAgent()
    test_dir = "test_cases"

    for fname in sorted(os.listdir(test_dir)):
        if not fname.endswith(".json"):
            continue
        path = os.path.join(test_dir, fname)

        try:
            data = load_json_multiencoding(path)
        except Exception as e:
            print(f"读取文件失败: {fname} - {e}")
            continue

        items = []
        if isinstance(data, list):
            items = data
        elif isinstance(data, dict):
            items = [data]
        else:
            print(f"跳过非预期格式: {fname}")
            continue

        for item in items:
            print(f"\n{'='*60}")
            print(f"文件: {fname}  题目ID: {item.get('question_id', 'unknown')}")
            q_text = item.get('question', '')
            print(f"题目: {q_text[:100]}{'...' if len(q_text)>100 else ''}")

            start_time = time.time()
            result = agent.solve(item)
            
            print(f"耗时: {elapsed:.2f} 秒")
            print(result)
            #print(f"答案: {result['answer']}")

            if 'answer' in item:
                expected = item['answer'].strip()
                predicted = result['answer'].strip()
                match = "✓" if expected == predicted else "✗"
                print(f"参考答案: {expected}")
                print(f"agent答案: {predicted}  {match}")

            print(f"{'='*60}")
            time.sleep(5)


if __name__ == "__main__":
    main()