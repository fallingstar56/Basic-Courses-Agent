# extract.py
# 实现 zhipuAI 调用接口，并提供处理 data/raw/ 高等微积分教程1.pdf 的入口。

from __future__ import annotations

import argparse
import json
import os
import re
import sys
from pathlib import Path
from typing import Any

try:
    import requests
except ImportError:  # pragma: no cover
    requests = None

try:
    from PyPDF2 import PdfReader
except ImportError:  # pragma: no cover
    PdfReader = None

DEFAULT_API_BASE = "https://api.zhipu.ai/v1/chat/completions"
DEFAULT_MODEL = "chatglm_pro"


class ZhipuAIClient:
    def __init__(self, api_key: str, model: str = DEFAULT_MODEL, api_base: str = DEFAULT_API_BASE) -> None:
        if not api_key:
            raise ValueError("zhipuAI API key is required")
        self.api_key = api_key.strip()
        self.model = model
        self.api_base = api_base.rstrip("/")

    def create_completion(
        self,
        content: str,
        temperature: float = 0.0,
        max_tokens: int = 2048,
        top_p: float = 1.0,
    ) -> str:
        payload = {
            "model": self.model,
            "messages": [{"role": "user", "content": content}],
            "temperature": temperature,
            "max_tokens": max_tokens,
            "top_p": top_p,
        }
        headers = {
            "Authorization": f"Bearer {self.api_key}",
            "Content-Type": "application/json",
        }
        response = self._post_json(self.api_base, payload, headers)
        return self._extract_response_text(response)

    def _post_json(self, url: str, payload: dict[str, Any], headers: dict[str, str]) -> dict[str, Any]:
        if requests is not None:
            resp = requests.post(url, headers=headers, json=payload, timeout=120)
            resp.raise_for_status()
            return resp.json()

        from urllib import request, error

        body = json.dumps(payload, ensure_ascii=False).encode("utf-8")
        req = request.Request(url, data=body, headers=headers, method="POST")
        try:
            with request.urlopen(req, timeout=120) as resp:
                raw = resp.read().decode("utf-8")
                return json.loads(raw)
        except error.HTTPError as exc:
            error_body = exc.read().decode("utf-8", errors="ignore")
            raise RuntimeError(f"HTTP error {exc.code}: {error_body}") from exc

    def _extract_response_text(self, response: dict[str, Any]) -> str:
        if not isinstance(response, dict):
            raise ValueError("zhipuAI response is not a JSON object")

        if "choices" in response and isinstance(response["choices"], list) and response["choices"]:
            first = response["choices"][0]
            if isinstance(first, dict):
                if "message" in first and isinstance(first["message"], dict):
                    return str(first["message"].get("content", "")).strip()
                if "text" in first:
                    return str(first.get("text", "")).strip()

        if "data" in response and isinstance(response["data"], list) and response["data"]:
            first = response["data"][0]
            if isinstance(first, dict) and "text" in first:
                return str(first["text"]).strip()

        if "text" in response:
            return str(response["text"]).strip()

        raise ValueError("Unable to extract text from zhipuAI response")


def extract_text_from_pdf(path: Path) -> str:
    if PdfReader is None:
        raise ImportError("读取 PDF 需要安装 PyPDF2。请运行: pip install PyPDF2")
    if not path.exists():
        raise FileNotFoundError(f"PDF 文件不存在: {path}")

    reader = PdfReader(path)
    pages: list[str] = []
    for page in reader.pages:
        pages.append(page.extract_text() or "")
    return "\n\n".join(pages).strip()


def extract_text(path: Path) -> str:
    suffix = path.suffix.lower()
    if suffix == ".pdf":
        return extract_text_from_pdf(path)
    raise ValueError("当前接口仅支持处理 .pdf 文件")


def is_end_marker_line(line: str) -> bool:
    stripped = line.strip()
    if not stripped:
        return False

    if re.fullmatch(r"[\s\|\-\u2500-\u257F]+", stripped) and len(stripped) >= 3:
        return True

    if re.search(r"[│┃┤├┌┐└┘].*[─━]|[─━].*[│┃┤├┌┐└┘]", stripped):
        return True

    return False


def split_question_blocks(content: str) -> list[dict[str, Any]]:
    question_pattern = re.compile(r"例\s*(\d+(?:\.\d+)*)")
    blocks: list[dict[str, Any]] = []

    current_block: dict[str, Any] | None = None
    for line in content.splitlines():
        match = question_pattern.search(line)
        if match:
            if current_block is not None:
                blocks.append(current_block)
            current_block = {
                "question_id": match.group(1),
                "lines": [line],
            }
            continue

        if current_block is not None:
            current_block["lines"].append(line)

    if current_block is not None:
        blocks.append(current_block)

    return blocks


def split_question_answer(block: dict[str, Any]) -> dict[str, str]:
    content = "\n".join(block["lines"]).strip()
    answer_start = None
    answer_keyword = None
    for match in re.finditer(r"(?m)^[ \t]*(证明|解)(?:[：:\s]|$)", content):
        answer_start = match.start()
        answer_keyword = match.group(1)
        break

    if answer_start is None:
        return {
            "question": content,
            "answer": "",
            "question_id": block["question_id"],
            "type": "数值计算",
        }

    question_text = content[:answer_start].strip()
    answer_text = content[answer_start:].strip()

    answer_lines = answer_text.splitlines()
    end_index = None
    for idx, line in enumerate(answer_lines):
        if is_end_marker_line(line):
            end_index = idx
            break
    if end_index is not None:
        answer_lines = answer_lines[:end_index]
    answer_text = "\n".join(answer_lines).strip()

    answer_prefix = answer_text.lstrip()
    if answer_prefix.startswith("证明"):
        q_type = "推导题"
    elif answer_prefix.startswith("解"):
        q_type = "数值计算"
    else:
        q_type = "数值计算"

    return {
        "question": question_text,
        "answer": answer_text,
        "question_id": block["question_id"],
        "type": q_type,
    }


def infer_difficulty(client: ZhipuAIClient, question_text: str) -> str:
    prompt = (
        "请判断以下高等微积分题目的难度，返回一个简短的中文标签：简单、中等、较难、困难。"
        " 只返回标签，不要添加解释。"
        f"\n题目：\n{question_text}"
    )
    response = client.create_completion(prompt, temperature=0.0, max_tokens=30)
    first_line = response.splitlines()[0].strip()
    return first_line or "中等"


def extract_questions_from_text(content: str, client: ZhipuAIClient) -> list[dict[str, str]]:
    blocks = split_question_blocks(content)
    questions: list[dict[str, str]] = []
    for block in blocks:
        item = split_question_answer(block)
        item["difficulty"] = infer_difficulty(client, item["question"]) if item["question"] else "中等"
        questions.append(item)
    return questions


def process_high_calculus_pdf(
    input_path: Path,
    api_key: str,
    model: str = DEFAULT_MODEL,
    temperature: float = 0.0,
) -> str:
    if not input_path.exists():
        raise FileNotFoundError(f"输入文件不存在: {input_path}")

    suffix = input_path.suffix.lower()
    if suffix != ".pdf":
        raise ValueError("当前接口仅支持处理 .pdf 文件")

    file_content = extract_text(input_path)
    client = ZhipuAIClient(api_key=api_key, model=model)
    questions = extract_questions_from_text(file_content, client)
    return json.dumps(questions, ensure_ascii=False, indent=2)


def save_json_output(content: str, output_path: Path) -> Path:
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(content, encoding="utf-8")
    return output_path


def parse_args() -> argparse.Namespace:
    default_input = Path(__file__).resolve().parents[1] / "data" / "raw" / "高等微积分教程1.pdf"
    default_output = Path(__file__).resolve().parents[1] / "data" / "processed" / "calculus1.json"
    parser = argparse.ArgumentParser(description="调用 zhipuAI 处理 data/raw/高等微积分教程1.pdf 并将结果输出到 processed 目录。")
    parser.add_argument("--api-key", help="zhipuAI API Key，可通过 ZHIPU_API_KEY 环境变量补充")
    parser.add_argument("--model", default=DEFAULT_MODEL, help="zhipuAI 模型名称")
    parser.add_argument("--input", type=Path, default=default_input, help="待处理的 .pdf 文件路径")
    parser.add_argument("--output", type=Path, default=default_output, help="输出汇总 JSON 文件路径")
    parser.add_argument("--temperature", type=float, default=0.0, help="生成温度")
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    api_key = args.api_key or os.getenv("ZHIPU_API_KEY")
    if not api_key:
        print("ERROR: 需要提供 zhipuAI API Key", file=sys.stderr)
        return 1

    try:
        output = process_high_calculus_pdf(
            input_path=args.input,
            api_key=api_key,
            model=args.model,
            temperature=args.temperature,
        )
        output_path = save_json_output(output, args.output)
        print(f"已生成题目汇总文件: {output_path}")
        return 0
    except Exception as exc:
        print(f"处理失败: {exc}", file=sys.stderr)
        return 2


if __name__ == "__main__":
    raise SystemExit(main())
