<<<<<<< HEAD
import os
import json
import dashscope
from dashscope import Generation

# ================= 配置区 =================
# 1. 填入你的 API KEY
dashscope.api_key = "sk-850fa1c48e184e67bf918820a750bb43" 

# 2. 直接在这里指定你要处理的 md 文件路径
TARGET_FILE = r"D:\weiyang city\Basic-Courses-Agent\data\processed\electric2\combined_result.md"  

# 3. 输出目录和文本分块参数
OUTPUT_DIR = r"D:\weiyang city\Basic-Courses-Agent\data\processed\electric2"  
CHUNK_SIZE = 2500  
OVERLAP = 500      

# 4. 从你的截图中挑选的顶尖模型
MODEL_NAME =  "qwen-plus"
# ==========================================

def read_markdown_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()

def chunk_text(text, chunk_size, overlap):
    chunks = []
    start = 0
    text_length = len(text)
    while start < text_length:
        end = start + chunk_size
        chunks.append(text[start:end])
        start += chunk_size - overlap
    return chunks

def extract_examples_from_chunk(text_chunk):
    system_prompt = """
    你是一个专业的理科教材数据清洗与结构化专家。
    用户会输入一段OCR识别的理科教材Markdown文本。请执行以下任务：

    1. 提取【带有完整解答】的例题。直接忽略只有题目没有解答的练习题或课后习题。
    2. 【反截断原则】：必须保证题目和解答提取完整。如果发现某个例题在文本结尾处被拦腰截断（话没说完），请尽可能通过语义补全，或者直接舍弃残缺部分。
    3. 【去噪清洗】：请自动过滤掉OCR识别带来的无关页码（如单独出现的四位数字 2764、3218 等）、行号或扫描乱码。
    4. 【格式保留】：严格保留原有的 LaTeX 数学公式和图片路径。对于图片标签，原样保留即可。

    请严格按照以下 JSON 数组格式输出：
    [
        {
            "question_id": "临时ID",
            "type": "推断题目类型（如：数值计算、证明题、概念辨析等）",
            "difficulty": "推断难度（如：基础、中等、困难）",
            "question": "完整的题目内容（包含原格式公式和图片，剔除杂质）",
            "answer": "完整的解答过程（包含原格式公式和图片，剔除杂质）"
        }
    ]
    如果没有符合条件的完整例题，请输出空数组：[]
    """

    messages = [
        {'role': 'system', 'content': system_prompt},
        {'role': 'user', 'content': f"请处理以下文本：\n\n{text_chunk}"}
    ]

    try:
        # 开启流式输出，防假死
        responses = Generation.call(
            model=MODEL_NAME,
            messages=messages,
            result_format='message',
            response_format={"type": "json_object"},
            stream=True, 
            incremental_output=True 
        )
        
        full_content = ""
        print("    [模型开始生成]:\n\033[90m", end="", flush=True) 
        
        for response in responses:
            if response.status_code == 200:
                chunk_text = response.output.choices[0]['message']['content']
                print(chunk_text, end="", flush=True)
                full_content += chunk_text
            else:
                print(f"\n\033[0mAPI 调用失败: {response.code} - {response.message}")
                return []
                
        print("\033[0m\n    [当前块生成完毕，正在校验数据...]")
        
        # 校验并解析 JSON
        content = full_content.strip()
        if content.startswith("```json"):
            content = content[7:-3].strip()
        elif content.startswith("```"):
            content = content[3:-3].strip()
            
        return json.loads(content)
            
    except Exception as e:
        print(f"\n\033[0m解析或调用异常: {e}")
        return []

def process_single_file(file_path):
    print(f"==== 开始处理文件: {file_path} ====")
    text = read_markdown_file(file_path)
    chunks = chunk_text(text, CHUNK_SIZE, OVERLAP)
    
    all_examples = []
    for i, chunk in enumerate(chunks):
        print(f"\n--- 正在处理第 {i+1}/{len(chunks)} 块文本 (长度: {len(chunk)}) ---")
        examples = extract_examples_from_chunk(chunk)
        if examples:
            # 强化拦截：丢掉答案为空或答案长度小于10个字符的残缺数据
            valid_examples = [ex for ex in examples if ex.get('answer') and len(str(ex.get('answer')).strip()) > 10]
            all_examples.extend(valid_examples)
            
    # 去重与重新编号
    unique_examples = []
    seen_questions = set()
    id_counter = 1
    
    for ex in all_examples:
        # 提取题目前30个字符作为指纹去重（过滤掉空格）
        q_snippet = ex.get('question', '').replace(" ", "")[:30] 
        
        # 必须是有效的非空题目
        if q_snippet not in seen_questions and len(q_snippet) > 5:
            seen_questions.add(q_snippet)
            
            # 统一格式化 ID (例如 EX_001, EX_002)
            ex["question_id"] = f"EX_{id_counter:03d}"
            id_counter += 1
            
            unique_examples.append(ex)
            
    return unique_examples

def main():
    if not os.path.exists(TARGET_FILE):
        print(f"❌ 错误：找不到文件 '{TARGET_FILE}'。请检查路径。")
        return

    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
        
    extracted_data = process_single_file(TARGET_FILE)
    
    base_name = os.path.basename(TARGET_FILE)
    output_filename = base_name.replace('.md', '_examples.json')
    output_path = os.path.join(OUTPUT_DIR, output_filename)
    
    # 格式化保存 JSON
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(extracted_data, f, ensure_ascii=False, indent=4)
        
    print(f"\n✅ 完成！共提取 {len(extracted_data)} 道高质量例题，已保存至:\n{os.path.abspath(output_path)}")

if __name__ == "__main__":
=======
import os
import json
import dashscope
from dashscope import Generation

# ================= 配置区 =================
# 1. 填入你的 API KEY
dashscope.api_key = "sk-850fa1c48e184e67bf918820a750bb43" 

# 2. 直接在这里指定你要处理的 md 文件路径
TARGET_FILE = r"D:\weiyang city\Basic-Courses-Agent\data\processed\electromagnetic\combined_result.md"  

# 3. 输出目录和文本分块参数
OUTPUT_DIR = r"D:\weiyang city\Basic-Courses-Agent\data\processed\electromagnetic"  
CHUNK_SIZE = 2500  
OVERLAP = 500      

# 4. 从你的截图中挑选的顶尖模型
MODEL_NAME =  "qwen3-max"
# ==========================================

def read_markdown_file(file_path):
    with open(file_path, 'r', encoding='utf-8') as f:
        return f.read()

def chunk_text(text, chunk_size, overlap):
    chunks = []
    start = 0
    text_length = len(text)
    while start < text_length:
        end = start + chunk_size
        chunks.append(text[start:end])
        start += chunk_size - overlap
    return chunks

def extract_examples_from_chunk(text_chunk):
    system_prompt = """
    你是一个专业的理科教材数据清洗与结构化专家。
    用户会输入一段OCR识别的理科教材Markdown文本。请执行以下任务：

    1. 提取【带有完整解答】的例题。直接忽略只有题目没有解答的练习题或课后习题。
    2. 【反截断原则】：必须保证题目和解答提取完整。如果发现某个例题在文本结尾处被拦腰截断（话没说完），请尽可能通过语义补全，或者直接舍弃残缺部分。
    3. 【去噪清洗】：请自动过滤掉OCR识别带来的无关页码（如单独出现的四位数字 2764、3218 等）、行号或扫描乱码。
    4. 【格式保留】：严格保留原有的 LaTeX 数学公式和图片路径。对于图片标签，原样保留即可。

    请严格按照以下 JSON 数组格式输出：
    [
        {
            "question_id": "临时ID",
            "type": "推断题目类型（如：数值计算、证明题、概念辨析等）",
            "difficulty": "推断难度（如：基础、中等、困难）",
            "question": "完整的题目内容（包含原格式公式和图片，剔除杂质）",
            "answer": "完整的解答过程（包含原格式公式和图片，剔除杂质）"
        }
    ]
    如果没有符合条件的完整例题，请输出空数组：[]
    """

    messages = [
        {'role': 'system', 'content': system_prompt},
        {'role': 'user', 'content': f"请处理以下文本：\n\n{text_chunk}"}
    ]

    try:
        # 开启流式输出，防假死
        responses = Generation.call(
            model=MODEL_NAME,
            messages=messages,
            result_format='message',
            response_format={"type": "json_object"},
            stream=True, 
            incremental_output=True 
        )
        
        full_content = ""
        print("    [模型开始生成]:\n\033[90m", end="", flush=True) 
        
        for response in responses:
            if response.status_code == 200:
                chunk_text = response.output.choices[0]['message']['content']
                print(chunk_text, end="", flush=True)
                full_content += chunk_text
            else:
                print(f"\n\033[0mAPI 调用失败: {response.code} - {response.message}")
                return []
                
        print("\033[0m\n    [当前块生成完毕，正在校验数据...]")
        
        # 校验并解析 JSON
        content = full_content.strip()
        if content.startswith("```json"):
            content = content[7:-3].strip()
        elif content.startswith("```"):
            content = content[3:-3].strip()
            
        return json.loads(content)
            
    except Exception as e:
        print(f"\n\033[0m解析或调用异常: {e}")
        return []

def process_single_file(file_path):
    print(f"==== 开始处理文件: {file_path} ====")
    text = read_markdown_file(file_path)
    chunks = chunk_text(text, CHUNK_SIZE, OVERLAP)
    
    all_examples = []
    for i, chunk in enumerate(chunks):
        print(f"\n--- 正在处理第 {i+1}/{len(chunks)} 块文本 (长度: {len(chunk)}) ---")
        examples = extract_examples_from_chunk(chunk)
        if examples:
            # 强化拦截：丢掉答案为空或答案长度小于10个字符的残缺数据
            valid_examples = [ex for ex in examples if ex.get('answer') and len(str(ex.get('answer')).strip()) > 10]
            all_examples.extend(valid_examples)
            
    # 去重与重新编号
    unique_examples = []
    seen_questions = set()
    id_counter = 1
    
    for ex in all_examples:
        # 提取题目前30个字符作为指纹去重（过滤掉空格）
        q_snippet = ex.get('question', '').replace(" ", "")[:30] 
        
        # 必须是有效的非空题目
        if q_snippet not in seen_questions and len(q_snippet) > 5:
            seen_questions.add(q_snippet)
            
            # 统一格式化 ID (例如 EX_001, EX_002)
            ex["question_id"] = f"EX_{id_counter:03d}"
            id_counter += 1
            
            unique_examples.append(ex)
            
    return unique_examples

def main():
    if not os.path.exists(TARGET_FILE):
        print(f"❌ 错误：找不到文件 '{TARGET_FILE}'。请检查路径。")
        return

    if not os.path.exists(OUTPUT_DIR):
        os.makedirs(OUTPUT_DIR)
        
    extracted_data = process_single_file(TARGET_FILE)
    
    base_name = os.path.basename(TARGET_FILE)
    output_filename = base_name.replace('.md', '_examples.json')
    output_path = os.path.join(OUTPUT_DIR, output_filename)
    
    # 格式化保存 JSON
    with open(output_path, 'w', encoding='utf-8') as f:
        json.dump(extracted_data, f, ensure_ascii=False, indent=4)
        
    print(f"\n✅ 完成！共提取 {len(extracted_data)} 道高质量例题，已保存至:\n{os.path.abspath(output_path)}")

if __name__ == "__main__":
>>>>>>> 7b30f784ba61d261b140f76ecea15327a1d60335
    main()