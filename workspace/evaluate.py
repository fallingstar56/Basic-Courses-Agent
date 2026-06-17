import os
import sys
import json
import time
import importlib
import re
from typing import Dict, Any, List

BASE_DIR = os.path.dirname(os.path.abspath(__file__))

# 配置路径。始终相对 evaluate.py 所在目录，避免从仓库根目录运行时误加载根目录 agent。
VAL_DATA_DIR = os.path.join(BASE_DIR, "val_data")
AGENT_DIR = os.path.join(BASE_DIR, "agent")
SUBMISSION_FILE = os.path.join(AGENT_DIR, "submission.json")
OUTPUT_RESULT_FILE = os.path.join(BASE_DIR, "evaluation_results.json")

def read_json_auto(filepath: str):
    """【新增】自动尝试多种编码读取 JSON 文件，彻底解决 utf-16/gbk 报错"""
    for enc in ['utf-8', 'utf-16', 'gbk', 'utf-8-sig', 'utf-16le']:
        try:
            with open(filepath, 'r', encoding=enc) as f:
                return json.load(f)
        except (UnicodeError, json.JSONDecodeError):
            continue
    print(f"无法解析或不支持的文件编码: {filepath}")
    return None

def load_validation_data() -> List[Dict[str, Any]]:
    """加载验证集题目"""
    items = []
    if not os.path.exists(VAL_DATA_DIR):
        print(f"未找到验证集目录: {VAL_DATA_DIR}")
        return items
        
    for fname in os.listdir(VAL_DATA_DIR):
        if fname.endswith(".json"):
            filepath = os.path.join(VAL_DATA_DIR, fname)
            data = read_json_auto(filepath)
            if data and isinstance(data, list):
                items.extend(data)
                
    print(f"共成功加载了 {len(items)} 道验证集题目。\n" + "="*50)
    return items

def main():
    print("="*50)
    print("极简本地模拟评测系统")
    print("="*50)
    
    # 1. 动态加载选手的 Agent
    sys.path.insert(0, os.path.abspath(AGENT_DIR))
    try:
        with open(SUBMISSION_FILE, 'r', encoding='utf-8') as f:
            config = json.load(f)
        module = importlib.import_module("agent") # 导入 agent.py
        agent_instance = getattr(module, config.get("entry_class", "MathAgent"))()
        solve_method = getattr(agent_instance, config.get("entry_method", "solve"))
        print(f"成功实例化智能体: {config.get('entry_class', 'MathAgent')}")
    except Exception as e:
        print(f"加载 Agent 失败: {e}")
        return

    # 2. 加载验证数据
    val_items = load_validation_data()
    results = []
    total_time = 0.0
    
    # 3. 逐题评测并实时输出
    for idx, item in enumerate(val_items, 1):
        q_id = item.get("question_id", f"Q_{idx}")
        print(f"\n▶ 正在评测 [{idx}/{len(val_items)}] 题目 ID: {q_id}")
        
        start_time = time.time()
        try:
            # 核心调用：给智能体传入数据
            response = solve_method(item)
            elapsed = time.time() - start_time
            total_time += elapsed

            if not isinstance(response, dict):
                raise TypeError(f"Agent 返回类型错误: {type(response).__name__}")
            
            ans = str(response.get("answer", "") or "")
            reasoning = str(response.get("reasoning_process", "") or "")
            truth = item.get("answer", "")
            output_error = None
            if not ans.strip() or not reasoning.strip():
                output_error = "empty_model_output"
            
            # 【终端实时可视化输出】
            print(f"   [耗时]: {elapsed:.2f} 秒")
            print(f"   [思考过程]:\n{reasoning}\n")
            print(f"   [模型答案]: {ans}")
            print(f"   [标准答案]: {truth}")
            if output_error:
                print(f"   [输出异常]: {output_error}")
            
            # 保存到结果列表
            results.append({
                "question_id": q_id,
                "truth_answer": truth,
                "pred_answer": ans,
                "reasoning_process": reasoning,
                "time_cost_seconds": round(elapsed, 2),
                "error": output_error
            })
            
        except Exception as e:
            elapsed = time.time() - start_time
            total_time += elapsed
            print(f"   [耗时]: {elapsed:.2f} 秒")
            print(f"   代码运行崩溃: {e}")
            
            results.append({
                "question_id": q_id,
                "truth_answer": item.get("answer", ""),
                "pred_answer": "",
                "reasoning_process": "",
                "time_cost_seconds": round(elapsed, 2),
                "error": str(e)
            })

    # 4. 落地为 JSON 汇总文件
    with open(OUTPUT_RESULT_FILE, "w", encoding="utf-8") as f:
        json.dump({
            "total_questions": len(val_items),
            "total_time_seconds": round(total_time, 2),
            "details": results
        }, f, ensure_ascii=False, indent=2)
        
    print("\n" + "="*50)
    print(f"💾 评测结束，已将全部输出（包含思考过程和答案）保存至: {OUTPUT_RESULT_FILE}")

if __name__ == "__main__":
    main()
