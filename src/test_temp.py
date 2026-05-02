from agent import MathAgent

# 准备题目数据（按照比赛要求的格式）
question_item = {
    "question_id": "001",
    "type": "微积分",
    "difficulty": "中等",
    "question": "求函数 f(x) = x^2 * sin(x) 的导数。",
    "image": None   # 可选
}

# 实例化 Agent（如果 combined_result_examples.json 不在当前目录，可以传入绝对路径）
agent = MathAgent(example_json_path=r"D:\weiyang city\Basic-Courses-Agent\data\processed\calculus1\combined_result_examples.json")

# 解题
result = agent.solve(question_item)

print("推理过程：")
print(result["reasoning_process"])
print("\n最终答案：")
print(result["answer"])