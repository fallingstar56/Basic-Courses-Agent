import base64
import os
import re
import shutil
import time
import requests
from PyPDF2 import PdfReader, PdfWriter

# ==================== 配置区域 ====================
API_URL = "https://b9zabar2f6bbw35c.aistudio-app.com/layout-parsing"
TOKEN = "b5ef3c1b24eff2120808f9aaa40a0da13617e0a0"

# 输入PDF路径和输出目录
PDF_PATH = r"D:\weiyang city\Basic-Courses-Agent\data\raw\量子物理.pdf"
OUTPUT_DIR = r"D:\weiyang city\Basic-Courses-Agent\data\processed\quantum"
TEMP_DIR = os.path.join(OUTPUT_DIR, "temp_parts")  # 临时存放拆分后的PDF
MERGE_IMAGES_DIR = "merged_images"                # 合并后图片存放的子目录

# 拆分参数
PAGES_PER_PART = 50

# API请求间隔（秒），避免请求过快
REQUEST_DELAY = 1

# ==================== 工具函数 ====================
def split_pdf(input_pdf, pages_per_part, output_dir):
    """将PDF拆分成每页数为pages_per_part的小文件，返回临时文件路径列表"""
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    else:
        # 清空临时目录
        for f in os.listdir(output_dir):
            os.remove(os.path.join(output_dir, f))

    reader = PdfReader(input_pdf)
    total_pages = len(reader.pages)
    part_files = []

    start = 0
    part_num = 0
    while start < total_pages:
        end = min(start + pages_per_part, total_pages) 
        writer = PdfWriter()
        for page_num in range(start, end):
            writer.add_page(reader.pages[page_num])
        part_path = os.path.join(output_dir, f"part_{part_num}.pdf")
        with open(part_path, "wb") as f:
            writer.write(f)
        part_files.append(part_path)
        start = end
        part_num += 1

    return part_files

def call_layout_api(file_path, api_url, token, optional_params):
    """调用布局解析API，返回响应JSON（或None）"""
    with open(file_path, "rb") as f:
        file_bytes = f.read()
        file_data = base64.b64encode(file_bytes).decode("ascii")

    headers = {
        "Authorization": f"token {token}",
        "Content-Type": "application/json"
    }
    required_payload = {
        "file": file_data,
        "fileType": 0,   # 0: PDF
    }
    payload = {**required_payload, **optional_params}

    try:
        resp = requests.post(api_url, json=payload, headers=headers, timeout=120)
        if resp.status_code == 200:
            return resp.json()
        else:
            print(f"API返回错误状态码 {resp.status_code}: {resp.text}")
            return None
    except Exception as e:
        print(f"API请求异常: {e}")
        return None

def save_part_result(part_index, api_result, output_dir):
    """
    保存单个小文件的解析结果到子目录 part_{part_index}
    返回子目录路径，以及该子目录下所有图片文件的路径映射（原路径 -> 新文件名）
    """
    part_dir = os.path.join(output_dir, f"part_{part_index}")
    os.makedirs(part_dir, exist_ok=True)

    result = api_result.get("result")
    if not result:
        print(f"part_{part_index}: 结果中没有 'result' 字段")
        return None

    layout_results = result.get("layoutParsingResults", [])
    if not layout_results:
        print(f"part_{part_index}: 没有 layoutParsingResults")
        return None

    # 保存Markdown文件
    for i, res in enumerate(layout_results):
        md_text = res.get("markdown", {}).get("text", "")
        md_filename = os.path.join(part_dir, f"page_{i}.md")
        with open(md_filename, "w", encoding="utf-8") as f:
            f.write(md_text)

        # 处理markdown中的图片（通过URL下载）
        images = res.get("markdown", {}).get("images", {})
        for img_path, img_url in images.items():
            # img_path 是相对路径，如 "images/1.png"
            full_img_path = os.path.join(part_dir, img_path)
            os.makedirs(os.path.dirname(full_img_path), exist_ok=True)
            try:
                img_resp = requests.get(img_url, timeout=30)
                if img_resp.status_code == 200:
                    with open(full_img_path, "wb") as f:
                        f.write(img_resp.content)
                else:
                    print(f"下载图片失败: {img_url}, 状态码 {img_resp.status_code}")
            except Exception as e:
                print(f"下载图片异常: {e}")

    # 处理 outputImages（如果存在）
    output_images = result.get("outputImages", {})
    for img_name, img_url in output_images.items():
        # 使用 img_name 作为文件名
        img_path = os.path.join(part_dir, img_name)
        try:
            img_resp = requests.get(img_url, timeout=30)
            if img_resp.status_code == 200:
                with open(img_path, "wb") as f:
                    f.write(img_resp.content)
            else:
                print(f"下载outputImage失败: {img_url}, 状态码 {img_resp.status_code}")
        except Exception as e:
            print(f"下载outputImage异常: {e}")

    return part_dir

def collect_images_and_update_md(part_dir, merged_images_dir, part_index, merged_md_file):
    """
    扫描 part_dir 下的所有图片，复制到 merged_images_dir 并重命名（加 part_index 前缀），
    同时读取该目录下的所有 .md 文件，替换其中的图片链接为新的相对路径，
    然后将处理后的内容写入 merged_md_file。
    """
    # 1. 扫描所有图片文件（递归查找）
    image_exts = ('.png', '.jpg', '.jpeg', '.gif', '.bmp', '.webp')
    image_map = {}  # 原路径 -> 新文件名（不含路径）
    for root, _, files in os.walk(part_dir):
        for f in files:
            if f.lower().endswith(image_exts):
                orig_path = os.path.relpath(os.path.join(root, f), part_dir)  # 相对于 part_dir 的路径
                # 生成唯一的新文件名：part_{index}_{原路径中的分隔符替换为下划线}
                safe_name = orig_path.replace('/', '_').replace('\\', '_')
                new_name = f"part_{part_index}_{safe_name}"
                image_map[orig_path] = new_name

                # 复制图片到 merged_images_dir
                src = os.path.join(root, f)
                dst = os.path.join(merged_images_dir, new_name)
                shutil.copy2(src, dst)

    # 2. 处理所有 .md 文件（按文件名排序）
    md_files = [f for f in os.listdir(part_dir) if f.endswith('.md')]
    md_files.sort(key=lambda x: int(x.split('_')[1].split('.')[0]) if '_' in x else 0)  # 假设格式 page_数字.md

    for md_file in md_files:
        md_path = os.path.join(part_dir, md_file)
        with open(md_path, 'r', encoding='utf-8') as f:
            content = f.read()

        # 替换图片链接
        def replace_link(match):
            # match.group(1) 是图片路径
            orig_path = match.group(1)
            # 去掉可能的前缀，比如 "./"
            orig_path = orig_path.lstrip('./')
            if orig_path in image_map:
                new_path = os.path.join(MERGE_IMAGES_DIR, image_map[orig_path]).replace('\\', '/')
                return f'![{match.group(2)}]({new_path})'
            else:
                # 如果找不到映射，保持原样（可能该图片不在本 part 中，但理论上应该在）
                return match.group(0)

        # 正则匹配图片链接：![alt](path)
        pattern = re.compile(r'!\[(.*?)\]\((.*?)\)')
        new_content = pattern.sub(replace_link, content)

        # 写入合并文件
        merged_md_file.write(new_content)
        merged_md_file.write('\n\n')  # 添加分隔

def main():
    # 创建临时目录和输出目录
    os.makedirs(OUTPUT_DIR, exist_ok=True)
    os.makedirs(TEMP_DIR, exist_ok=True)
    merged_images_path = os.path.join(OUTPUT_DIR, MERGE_IMAGES_DIR)
    os.makedirs(merged_images_path, exist_ok=True)

    # 1. 拆分PDF
    print("正在拆分PDF...")
    part_files = split_pdf(PDF_PATH, PAGES_PER_PART, TEMP_DIR)
    print(f"拆分成 {len(part_files)} 个小文件")

    # 2. 依次处理每个小文件
    part_dirs = []
    optional_params = {
        "useDocOrientationClassify": False,
        "useDocUnwarping": False,
        "useChartRecognition": False,
    }

    for idx, pdf_path in enumerate(part_files):
        print(f"\n处理第 {idx+1}/{len(part_files)} 个文件: {os.path.basename(pdf_path)}")
        api_result = call_layout_api(pdf_path, API_URL, TOKEN, optional_params)
        if api_result is None:
            print(f"跳过文件 {pdf_path}")
            continue

        part_dir = save_part_result(idx, api_result, OUTPUT_DIR)
        if part_dir:
            part_dirs.append((idx, part_dir))
        else:
            print(f"第 {idx} 部分保存失败")

        time.sleep(REQUEST_DELAY)  # 避免请求过快

    # 3. 合并结果
    if not part_dirs:
        print("没有成功处理的部分，合并终止")
        return

    print("\n开始合并结果...")
    final_md_path = os.path.join(OUTPUT_DIR, "combined_result.md")
    with open(final_md_path, 'w', encoding='utf-8') as final_md:
        for idx, part_dir in sorted(part_dirs, key=lambda x: x[0]):
            print(f"合并 part_{idx}")
            collect_images_and_update_md(part_dir, merged_images_path, idx, final_md)

    print(f"\n合并完成！最终Markdown文件: {final_md_path}")
    print(f"所有图片已保存到: {merged_images_path}")

  
    shutil.rmtree(TEMP_DIR)  # 取消注释以删除临时PDF
    # 注意：part_dirs 中的子目录也可以删除，但为了保留中间结果，这里不自动删除

if __name__ == "__main__":
    main()