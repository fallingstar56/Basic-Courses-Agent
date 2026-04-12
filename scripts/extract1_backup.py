import os
import re
import json
from difflib import SequenceMatcher

import dashscope
from dashscope import Generation

# ================= Configuration =================
# Prefer env var for safety: set DASHSCOPE_API_KEY in your shell.
DASHSCOPE_API_KEY = "sk-44a40e2bf4484b12b8056cf286c4e73a"
dashscope.api_key = DASHSCOPE_API_KEY
    
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))

TARGET_FILE = os.path.join(BASE_DIR, r"data\processed\calculus1\combined_result.md")
OUTPUT_DIR = os.path.join(BASE_DIR, r"data\processed\calculus1")

MODEL_NAME = "qwen3-max"

# Stage-1 candidate recall config
RECALL_BATCH_SIZE = 12
MAX_PREVIEW_CHARS = 380

# Stage-2 extraction context config
NEIGHBOR_CHARS = 500
MIN_ANSWER_CHARS = 20
MIN_QUESTION_CHARS = 12

# Dedup config
SIMILARITY_THRESHOLD = 0.92

# Optional LLM review stage after rule checks
ENABLE_LLM_REVIEW = False
# =================================================


def read_markdown_file(file_path):
    with open(file_path, "r", encoding="utf-8") as f:
        return f.read()


def normalize_newlines(text):
    return text.replace("\r\n", "\n").replace("\r", "\n")


def split_by_paragraphs(text):
    text = normalize_newlines(text)
    parts = re.split(r"\n\s*\n+", text)
    return [p.strip() for p in parts if p.strip()]


def is_structural_boundary(paragraph):
    heading = bool(re.match(r"^#{1,6}\s+", paragraph))
    chapter_style = bool(re.match(r"^(第[一二三四五六七八九十0-9]+[章节讲]|[0-9]+\.[0-9]+)", paragraph))
    example_start = bool(re.search(r"(^|\n)\s*(例\s*题|例\s*[0-9一二三四五六七八九十]+|Example)\b", paragraph, flags=re.IGNORECASE))
    return heading or chapter_style or example_start


def build_semantic_segments(text, max_chars=1800, min_chars=500):
    """
    Build semantically-friendly segments from paragraphs instead of rigid fixed-size chunks.
    """
    paragraphs = split_by_paragraphs(text)
    segments = []
    current = []
    current_len = 0

    for p in paragraphs:
        p_len = len(p)
        boundary = is_structural_boundary(p)

        # If paragraph is too long, keep it as its own segment to avoid losing structure.
        if p_len > max_chars:
            if current:
                segments.append("\n\n".join(current))
                current = []
                current_len = 0
            segments.append(p)
            continue

        should_flush = False
        if current and current_len >= min_chars and boundary:
            should_flush = True
        if current and (current_len + p_len + 2) > max_chars:
            should_flush = True

        if should_flush:
            segments.append("\n\n".join(current))
            current = [p]
            current_len = p_len
        else:
            current.append(p)
            current_len += p_len + 2

    if current:
        segments.append("\n\n".join(current))

    return segments


def parse_json_from_text(raw_text):
    text = raw_text.strip()

    # Strip markdown fences if present.
    if text.startswith("```"):
        text = re.sub(r"^```(?:json)?", "", text).strip()
        if text.endswith("```"):
            text = text[:-3].strip()

    # Try direct JSON parse first.
    try:
        return json.loads(text)
    except Exception:
        pass

    # Fallback: find first top-level JSON object or array.
    obj_match = re.search(r"\{[\s\S]*\}", text)
    arr_match = re.search(r"\[[\s\S]*\]", text)

    candidate = None
    if obj_match and arr_match:
        candidate = arr_match.group(0) if arr_match.start() < obj_match.start() else obj_match.group(0)
    elif obj_match:
        candidate = obj_match.group(0)
    elif arr_match:
        candidate = arr_match.group(0)

    if candidate is None:
        raise ValueError("No JSON object/array found in model output.")

    return json.loads(candidate)


def call_model(messages, expect_json=True, stream=True):
    if not dashscope.api_key:
        raise RuntimeError("dashscope.api_key is empty. Please set DASHSCOPE_API_KEY.")

    kwargs = {
        "model": MODEL_NAME,
        "messages": messages,
        "result_format": "message",
    }

    if expect_json:
        kwargs["response_format"] = {"type": "json_object"}

    if stream:
        kwargs["stream"] = True
        kwargs["incremental_output"] = True

    responses = Generation.call(**kwargs)

    content = ""
    if stream:
        for response in responses:
            if response.status_code == 200:
                content += response.output.choices[0]["message"]["content"]
            else:
                raise RuntimeError(f"API failed: {response.code} - {response.message}")
    else:
        if responses.status_code != 200:
            raise RuntimeError(f"API failed: {responses.code} - {responses.message}")
        content = responses.output.choices[0]["message"]["content"]

    return content


def iter_batches(items, batch_size):
    for i in range(0, len(items), batch_size):
        yield items[i:i + batch_size]


def stage1_recall_candidates(segments):
    """
    Stage-1: high-recall candidate detection from semantic segments.
    Return set of candidate segment indices.
    """
    candidate_ids = set()

    for batch in iter_batches(list(enumerate(segments)), RECALL_BATCH_SIZE):
        payload = []
        for sid, seg in batch:
            preview = seg[:MAX_PREVIEW_CHARS]
            payload.append({"segment_id": sid, "preview": preview})

        user_input = json.dumps(payload, ensure_ascii=False)

        system_prompt = """
你是教材例题召回助手。目标是高召回，不要漏掉可能含有“完整题目+完整解答”的段落。
输入是若干段文本预览，每段有 segment_id 和 preview。
规则：
1) 只要看起来可能是“例题/例/Example + 解答/解/解析”的，就标为候选。
2) 如果不确定，也优先保留为候选。
3) 忽略纯目录、纯页码、纯标题、纯练习题列表（无解答）。
请输出严格 JSON 对象：
{
  "candidate_ids": [0, 1, 2]
}
""".strip()

        messages = [
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": f"请判断以下段落预览的候选ID：\n{user_input}"},
        ]

        try:
            raw = call_model(messages, expect_json=True, stream=False)
            data = parse_json_from_text(raw)
            ids = data.get("candidate_ids", []) if isinstance(data, dict) else []
            for x in ids:
                if isinstance(x, int) and 0 <= x < len(segments):
                    candidate_ids.add(x)
        except Exception as e:
            print(f"[Stage-1 warning] candidate recall failed in one batch: {e}")

    # If recall fails entirely, safely fallback to all segments.
    if not candidate_ids:
        candidate_ids = set(range(len(segments)))

    return sorted(candidate_ids)


def join_with_neighbors(segments, idx, neighbor_chars=NEIGHBOR_CHARS):
    left = segments[idx - 1][-neighbor_chars:] if idx - 1 >= 0 else ""
    mid = segments[idx]
    right = segments[idx + 1][:neighbor_chars] if idx + 1 < len(segments) else ""

    parts = []
    if left:
        parts.append("[LEFT_NEIGHBOR]\n" + left)
    parts.append("[TARGET_SEGMENT]\n" + mid)
    if right:
        parts.append("[RIGHT_NEIGHBOR]\n" + right)

    return "\n\n".join(parts)


def stage2_extract_examples(context_text):
    """
    Stage-2: strict extraction from a candidate context window.
    """
    system_prompt = """
你是理科教材数据清洗与结构化专家。请从输入文本中提取“带完整解答的例题”。
要求：
1) 仅保留“题目+解答完整”的例题；无解答或明显残缺的不要。
2) 自动去除 OCR 噪声（页码、行号、乱码）。
3) 尽量保留原始公式与图片标签。
4) 不要编造不存在的内容。
严格输出 JSON 对象：
{
  "examples": [
    {
      "question_id": "TEMP",
      "type": "题型",
      "difficulty": "基础|中等|困难",
      "question": "...",
      "answer": "..."
    }
  ]
}
无结果时输出：{"examples": []}
""".strip()

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": f"请处理以下文本：\n\n{context_text}"},
    ]

    raw = call_model(messages, expect_json=True, stream=True)
    data = parse_json_from_text(raw)

    if isinstance(data, dict):
        items = data.get("examples", [])
    elif isinstance(data, list):
        items = data
    else:
        items = []

    return items if isinstance(items, list) else []


def lightweight_rule_validate(ex):
    question = str(ex.get("question", "")).strip()
    answer = str(ex.get("answer", "")).strip()

    if len(question) < MIN_QUESTION_CHARS:
        return False
    if len(answer) < MIN_ANSWER_CHARS:
        return False

    # Basic anti-noise guard: reject pure number noise.
    pure_number_line = re.fullmatch(r"[0-9\s]+", question)
    if pure_number_line:
        return False

    return True


def llm_review_example(ex):
    """
    Optional strict reviewer to filter incomplete or mismatched Q/A pairs.
    """
    if not ENABLE_LLM_REVIEW:
        return True

    payload = {
        "question": ex.get("question", ""),
        "answer": ex.get("answer", ""),
    }

    system_prompt = """
你是例题质检器。检查题目与解答是否完整且匹配。
输出严格 JSON 对象：{"pass": true/false, "reason": "..."}
判定标准：
1) 题目是否明显残缺。
2) 解答是否针对该题目。
3) 解答是否过短或只有片段。
""".strip()

    messages = [
        {"role": "system", "content": system_prompt},
        {"role": "user", "content": json.dumps(payload, ensure_ascii=False)},
    ]

    try:
        raw = call_model(messages, expect_json=True, stream=False)
        data = parse_json_from_text(raw)
        return bool(data.get("pass", False)) if isinstance(data, dict) else False
    except Exception as e:
        print(f"[Review warning] LLM review failed, fallback to pass=True: {e}")
        return True


def normalize_for_fingerprint(text):
    t = str(text or "")
    t = t.lower()
    t = re.sub(r"\s+", "", t)
    t = t.replace("（", "(").replace("）", ")")
    t = t.replace("，", ",").replace("。", ".")
    return t


def is_duplicate_question(new_q_norm, existed_norm_list):
    if not new_q_norm:
        return True

    for old in existed_norm_list:
        if new_q_norm == old:
            return True
        sim = SequenceMatcher(None, new_q_norm, old).ratio()
        if sim >= SIMILARITY_THRESHOLD:
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
        if not llm_review_example(ex):
            continue

        q_norm = normalize_for_fingerprint(ex.get("question", ""))
        if is_duplicate_question(q_norm, seen_norm):
            continue

        seen_norm.append(q_norm)

        ex_out = {
            "question_id": f"EX_{counter:03d}",
            "type": str(ex.get("type", "未分类")).strip() or "未分类",
            "difficulty": str(ex.get("difficulty", "中等")).strip() or "中等",
            "question": str(ex.get("question", "")).strip(),
            "answer": str(ex.get("answer", "")).strip(),
        }
        clean.append(ex_out)
        counter += 1

    return clean


def process_single_file(file_path):
    print(f"==== Start processing: {file_path} ====")
    text = read_markdown_file(file_path)

    # Step A: semantic segmentation
    segments = build_semantic_segments(text)
    print(f"[A] semantic segments: {len(segments)}")

    # Step B: candidate recall
    candidate_ids = stage1_recall_candidates(segments)
    print(f"[B] recalled candidate segments: {len(candidate_ids)}")

    # Step C: strict extraction with neighbor window
    all_examples = []
    for i, seg_id in enumerate(candidate_ids, start=1):
        print(f"[C] extracting {i}/{len(candidate_ids)} from segment {seg_id}")
        context_text = join_with_neighbors(segments, seg_id, NEIGHBOR_CHARS)
        try:
            items = stage2_extract_examples(context_text)
            all_examples.extend(items)
        except Exception as e:
            print(f"[C warning] extraction failed for segment {seg_id}: {e}")

    print(f"[C] raw extracted examples: {len(all_examples)}")

    # Step D: validate + review + dedup + reindex
    final_examples = post_process_and_dedup(all_examples)
    print(f"[D] final examples after filtering/dedup: {len(final_examples)}")

    return final_examples


def main():
    if not dashscope.api_key:
        print("❌ Missing API key. Please set DASHSCOPE_API_KEY in environment.")
        return

    if not os.path.exists(TARGET_FILE):
        print(f"❌ File not found: {TARGET_FILE}")
        return

    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)

    extracted_data = process_single_file(TARGET_FILE)

    base_name = os.path.basename(TARGET_FILE)
    output_filename = base_name.replace(".md", "_examples_new.json")
    output_path = os.path.join(OUTPUT_DIR, output_filename)

    with open(output_path, "w", encoding="utf-8") as f:
        json.dump(extracted_data, f, ensure_ascii=False, indent=2)

    print(f"✅ Done. Extracted {len(extracted_data)} examples -> {os.path.abspath(output_path)}")


if __name__ == "__main__":
    main()
