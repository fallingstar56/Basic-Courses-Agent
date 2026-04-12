import os
import re
import json
import bisect
from difflib import SequenceMatcher

from zhipuai import ZhipuAI

# ================= Configuration =================
ZHIPU_API_KEY = "aaddd9dd952a437b8b1106d0da287e03.M68vPwu2NYG1GCCd"  
client = ZhipuAI(api_key=ZHIPU_API_KEY)

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

TARGET_FILE = os.path.join(BASE_DIR, r"data\processed\calculus1\combined_result.md")
OUTPUT_DIR = os.path.join(BASE_DIR, r"data\processed\calculus1")

MODEL_NAME = "glm-4-plus"

MIN_ANSWER_CHARS = 20
MIN_QUESTION_CHARS = 12
SIMILARITY_THRESHOLD = 0.92

# Max chars per LLM batch (combine small blocks to save API calls)
LLM_BATCH_MAX_CHARS = 6000
# =================================================


# =============== Regex Patterns ===============
# Example header at line start:  > 例 1.1.1, #### > 例 1.3.3, 例 2-1, 例2.1.10
EXAMPLE_HEADER_RE = re.compile(
    r'^[ \t]*(?:#{1,6}\s+)?(?:▶\s*)?例\s*(\d+[\.\-]\d+(?:[\.\-]\d+)?)',
    re.MULTILINE,
)

# Structural boundaries that terminate an example block
STOP_RE = re.compile(
    r'^[ \t]*(?:#{1,6}\s+)?(?:习题\s*\d|总复习题|第\s*[一二三四五六七八九十\d]+\s*章)',
    re.MULTILINE,
)
# ==============================================


def read_markdown_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read().replace("\r\n", "\n").replace("\r", "\n")


def parse_json_from_text(raw_text):
    text = raw_text.strip()
    if text.startswith("`" + ""):
        text = re.sub(r"^`" + "(?:json)?", "", text).strip()
        if text.endswith("`" + ""):
            text = text[:-3].strip()
    try:
        return json.loads(text)
    except Exception:
        pass
    for pat in [r"\[[\s\S]*\]", r"\{[\s\S]*\}"]:
        m = re.search(pat, text)
        if m:
            try:
                return json.loads(m.group(0))
            except Exception:
                continue
    raise ValueError("No JSON found in model output.")


def call_model(messages, expect_json=True, stream=True):
    if not ZHIPU_API_KEY or ZHIPU_API_KEY == "YOUR_ZHIPU_API_KEY":
        raise RuntimeError("ZHIPU_API_KEY is empty. Please fill in your API key.")
    kwargs = {
        "model": MODEL_NAME,
        "messages": messages,
    }
    if expect_json:
        kwargs["response_format"] = {"type": "json_object"}
    if stream:
        kwargs["stream"] = True
        response = client.chat.completions.create(**kwargs)
        content = ""
        for chunk in response:
            delta = chunk.choices[0].delta
            if delta.content:
                content += delta.content
    else:
        response = client.chat.completions.create(**kwargs)
        content = response.choices[0].message.content
    return content


# =============== Core: Regex-Based Example Block Extraction ===============

def find_example_blocks(text):
    """
    Use regex to locate all 'example X.Y.Z' headers, then extract the text block
    from each header to the next header or structural boundary.
    This guarantees only example content is extracted -- no exercise contamination.
    """
    headers = [(m.start(), m.group(1)) for m in EXAMPLE_HEADER_RE.finditer(text)]
    if not headers:
        print("[Warning] No example headers found in text.")
        return []

    boundaries = [m.start() for m in STOP_RE.finditer(text)]

    # All positions where a block should end: next example header, boundary, or EOF
    end_markers = sorted(set([pos for pos, _ in headers] + boundaries + [len(text)]))

    blocks = []
    for start, eid in headers:
        idx = bisect.bisect_right(end_markers, start)
        end = end_markers[idx] if idx < len(end_markers) else len(text)
        block_text = text[start:end].strip()
        if block_text:
            blocks.append({"id": eid, "text": block_text})

    return blocks


# =============== LLM-Based Q/A Extraction ===============

EXTRACT_SYSTEM_PROMPT = """
你是理科教材例题提取专家。请从以下文本中提取每道例题的题目(question)和解答(answer)。

**核心规则：**
1) 每个"例 X.Y.Z"编号对应JSON中的一个条目，question_id填写该编号（如"1.1.1"）。
2) question 是题目的完整叙述（求证什么、求什么、考察什么）。
3) answer 是解答/证明/分析的完整内容。
4) 有些例题没有显式的"解"或"证明"标记——请根据语义推理判断哪部分是题目、哪部分是解答。
   - 如果例题本身是"举例说明"类型（如"求以下数集的上下确界"后直接给出结果），则 question 是要求，answer 是具体的举例和说明。
   - 如果整段都是陈述性说明（如"函数sinx不是R上的单调函数，但..."），则 question 是"考察/说明什么"，answer 是具体内容。
5) **绝对禁止**提取习题、练习题、思考题。只提取正式的"例"。
6) **格式要求（极其重要）：question 和 answer 的内容必须使用 Markdown 格式：**
   - 数学公式必须保留原始LaTeX格式，行内公式用 `$ ... $`，行间公式用 `$$ ... $$`。
   - **严禁**将LaTeX公式转为纯文本（如写成 lim_{n→∞} 或 √[n]{n}）。必须写成 `$\\lim_{n\\to\\infty}$` 或 `$\\sqrt[n]{n}$`。
   - 保留换行：多步骤推导之间用换行分隔。
   - 保留图片标签（如 `<img ...>` 标签）。
   - 去除页码、行号等OCR噪声。
7) 不要编造不存在的内容。如果文本中确实没有例题，返回空列表。

输出严格JSON：
{
  "examples": [
    {"question_id": "1.1.1", "question": "Markdown格式的完整题目", "answer": "Markdown格式的完整解答"}
  ]
}
无例题则输出：{"examples": []}
""".strip()


def llm_extract_batch(blocks_text):
    """
    Send one or more example blocks to LLM for Q/A extraction.
    """
    messages = [
        {"role": "system", "content": EXTRACT_SYSTEM_PROMPT},
        {"role": "user", "content": f"请提取以下文本中每道例题的题目和解答：\n\n{blocks_text}"},
    ]
    try:
        raw = call_model(messages, expect_json=True, stream=True)
        data = parse_json_from_text(raw)
        items = data.get("examples", []) if isinstance(data, dict) else []
        return items if isinstance(items, list) else []
    except Exception as e:
        print(f"  [LLM error] {e}")
        return []


def extract_all(blocks):
    """
    Batch blocks together (up to LLM_BATCH_MAX_CHARS) and send to LLM.
    Each 例 X.X.X is guaranteed to become a JSON unit.
    """
    results = []
    batch_text = ""
    batch_ids = []
    batch_start = 0

    def flush_batch():
        nonlocal batch_text, batch_ids, batch_start
        if not batch_text:
            return
        id_range = f"{batch_ids[0]}~{batch_ids[-1]}" if len(batch_ids) > 1 else batch_ids[0]
        print(f"  [LLM] Extracting batch: 例 {id_range} ({len(batch_text)} chars, {len(batch_ids)} blocks)")
        items = llm_extract_batch(batch_text)
        if items:
            results.extend(items)
            print(f"    -> Got {len(items)} examples")
        else:
            print(f"    -> No examples returned")
        batch_text = ""
        batch_ids = []

    for i, b in enumerate(blocks):
        eid, text = b["id"], b["text"]
        print(f"  [{i+1}/{len(blocks)}] 例 {eid}: {len(text)} chars")

        # If adding this block would exceed limit, flush current batch first
        if batch_text and len(batch_text) + len(text) + 10 > LLM_BATCH_MAX_CHARS:
            flush_batch()

        separator = f"\n\n{'='*40}\n\n" if batch_text else ""
        batch_text += separator + text
        batch_ids.append(eid)

    # Flush remaining
    flush_batch()

    return results


# =============== Validation & Dedup ===============

def lightweight_rule_validate(ex):
    question = str(ex.get("question", "")).strip()
    answer = str(ex.get("answer", "")).strip()
    if len(question) < MIN_QUESTION_CHARS:
        return False
    if len(answer) < MIN_ANSWER_CHARS:
        return False
    if re.fullmatch(r"[0-9\s]+", question):
        return False
    return True


def normalize_for_fingerprint(text):
    t = str(text or "").lower()
    t = re.sub(r"\s+", "", t)
    for old, new in [("（", "("), ("）", ")"), ("，", ","), ("。", ".")]:
        t = t.replace(old, new)
    return t


def is_duplicate_question(new_q_norm, existed_norm_list):
    if not new_q_norm:
        return True
    for old in existed_norm_list:
        if new_q_norm == old:
            return True
        if SequenceMatcher(None, new_q_norm, old).ratio() >= SIMILARITY_THRESHOLD:
            return True
    return False


def post_process_and_dedup(examples):
    clean = []
    seen_norm = []
    counter = 1

    for ex in examples:
        if not isinstance(ex, dict):
            continue
        if not lightweight_rule_validate(ex):
            continue

        q_norm = normalize_for_fingerprint(ex.get("question", ""))
        if is_duplicate_question(q_norm, seen_norm):
            continue
        seen_norm.append(q_norm)

        clean.append({
            "question_id": f"EX_{counter:03d}",
            "source_id": str(ex.get("question_id", "")).strip(),
            "question": str(ex.get("question", "")).strip(),
            "answer": str(ex.get("answer", "")).strip(),
        })
        counter += 1

    return clean


# =============== Pipeline ===============

def process_single_file(file_path):
    print(f"==== Processing: {file_path} ====")
    text = read_markdown_file(file_path)

    # Step A: regex-based example block extraction (precise, no exercises)
    blocks = find_example_blocks(text)
    print(f"[A] Found {len(blocks)} example blocks via regex")
    for b in blocks:
        print(f"    例 {b['id']}: {len(b['text'])} chars")

    # Step B: extract Q/A from each block
    all_examples = extract_all(blocks)
    print(f"[B] Extracted {len(all_examples)} raw examples")

    # Step C: validate + dedup
    final_examples = post_process_and_dedup(all_examples)
    print(f"[C] Final: {len(final_examples)} examples after validation/dedup")

    return final_examples


def main():
    if not ZHIPU_API_KEY or ZHIPU_API_KEY == "YOUR_ZHIPU_API_KEY":
        print("Missing API key. Please set ZHIPU_API_KEY in extract1.py.")
        return

    if not os.path.exists(TARGET_FILE):
        print(f"File not found: {TARGET_FILE}")
        return

    os.makedirs(OUTPUT_DIR, exist_ok=True)

    extracted_data = process_single_file(TARGET_FILE)

    base_name = os.path.basename(TARGET_FILE)
    output_filename = base_name.replace(".md", "_examples_new.json")
    output_path = os.path.join(OUTPUT_DIR, output_filename)

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(extracted_data, f, ensure_ascii=False, indent=2)

    print(f"Done. Extracted {len(extracted_data)} examples -> {os.path.abspath(output_path)}")


if __name__ == "__main__":
    main()
