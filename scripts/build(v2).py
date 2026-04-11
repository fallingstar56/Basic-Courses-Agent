import json
import faiss
import hashlib
import numpy as np
from pathlib import Path
from sentence_transformers import SentenceTransformer

# ================= 核心功能 1：全局唯一 ID 生成 =================
def generate_global_id(file_path, question_id):
    """
    通过【文件绝对路径】+【题目原始ID】生成唯一的MD5哈希值。
    这保证了即使不同子文件夹里的 JSON 都有 "EX_001"，生成的 ID 也是唯一的。
    """
    combined_str = f"{file_path}_{question_id}"
    return hashlib.md5(combined_str.encode()).hexdigest()

# ================= 核心功能 2：智能文本切片 =================
def chunk_text(text, max_chars=600, overlap=100):
    """
    将题目和答案合并后的长文本切分为小块（Chunk）。
    overlap 参数保留了相邻切片之间的重叠，防止数学公式或逻辑在中途被切断。
    """
    if len(text) <= max_chars:
        return [text]
    
    chunks = []
    start = 0
    while start < len(text):
        end = start + max_chars
        chunks.append(text[start:end])
        # 窗口向前滑动：步长 = 窗口大小 - 重叠大小
        start += (max_chars - overlap)
    return chunks

def load_and_process_data(search_root, target_filename):
    """
    递归扫描子文件夹并处理数据。
    """
    root_path = Path(search_root).resolve()
    print(f"🔍 正在扫描根目录: {root_path}")
    
    # 使用 rglob('*') 递归查找所有层级下的目标文件名
    found_files = list(root_path.rglob(target_filename))
    
    if not found_files:
        print(f"❌ 错误：在 {root_path} 下未找到任何名为 {target_filename} 的文件。")
        return [], {}

    all_chunks_metadata = [] 
    full_records_map = {}    

    for filepath in found_files:
        print(f"📄 正在处理文件: {filepath.relative_to(root_path)}")
        with open(filepath, 'r', encoding='utf-8') as f:
            try:
                data = json.load(f)
                for item in data:
                    # 获取原始 ID
                    original_id = item.get('question_id', 'unknown')
                    # 生成全局唯一 Hash ID
                    global_id = generate_global_id(str(filepath), original_id)
                    
                    # 补充元数据
                    item['global_id'] = global_id
                    item['source_file'] = str(filepath)
                    full_records_map[global_id] = item

                    # 整合检索内容
                    combined_content = f"题目: {item.get('question','')}\n答案: {item.get('answer','')}"
                    
                    # 执行切片
                    chunks = chunk_text(combined_content)
                    for i, text_chunk in enumerate(chunks):
                        all_chunks_metadata.append({
                            "parent_id": global_id,
                            "chunk_index": i,
                            "vector_text": text_chunk # 实际用于生成向量的文本
                        })
            except Exception as e:
                print(f"⚠️ 跳过文件 {filepath}，读取失败: {e}")

    return all_chunks_metadata, full_records_map

def build_faiss_index(chunks_meta, save_path):
    """
    构建并保存向量库。
    """
    if not chunks_meta:
        return None, None

    print(f"🚀 正在为 {len(chunks_meta)} 个文本切片生成向量...")
    model = SentenceTransformer('paraphrase-multilingual-MiniLM-L12-v2')
    
    # 提取切片文本并转化为向量
    texts = [c['vector_text'] for c in chunks_meta]
    embeddings = model.encode(texts, show_progress_bar=True)
    embeddings = np.array(embeddings).astype('float32')
    
    # 创建 FAISS 索引
    dimension = embeddings.shape[1]
    index = faiss.IndexFlatL2(dimension)
    index.add(embeddings)
    
    # 保存到磁盘
    faiss.write_index(index, save_path)
    print(f"✅ 向量库已保存至: {save_path}")
    return index, model

# ================= 主程序执行 =================
if __name__ == "__main__":
    # --- 路径自动定位策略 ---
    # 获取当前运行的 py 脚本所在的目录 (scripts 文件夹)
    current_script_dir = Path(__file__).resolve().parent
    # 定位到它的上一级目录 (Basic-Courses-Agent 根目录)
    project_root = current_script_dir.parent
    
    # 设置你要扫描的起始文件夹（假设 JSON 都在根目录下的某个地方）
    # 如果就在根目录下找，直接写 project_root
    SEARCH_ROOT = project_root 
    
    TARGET_FILE = "combined_result_examples.json"
    INDEX_FILE = str(project_root / "unified_math_index.faiss")

    # 1. 扫描并处理数据
    chunks_meta, full_map = load_and_process_data(SEARCH_ROOT, TARGET_FILE)

    if chunks_meta:
        # 2. 构建向量库
        idx, embed_model = build_faiss_index(chunks_meta, INDEX_FILE)
        
        # 3. 简单验证检索
        query = "Stolz 定理的应用"
        print(f"\n测试检索: {query}")
        q_vec = embed_model.encode([query]).astype('float32')
        D, I = idx.search(q_vec, k=1)
        
        parent_id = chunks_meta[I[0][0]]['parent_id']
        result = full_map[parent_id]
        print(f"找到最相关题目来自: {result['source_file']}")
        print(f"题目内容: {result['question'][:100]}...")