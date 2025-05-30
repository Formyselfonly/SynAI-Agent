# memory_update_demo.py
import datetime
import json

# 初始化用户记忆结构
user_memory = {
    "emo_room": [],  # 存储情绪、人际关系、事件、时间等信息
    "trends": []   # 存储情绪的变化趋势，如“焦虑 -> 改善”
}

# 记录情绪函数：将用户输入中的人际关系、情绪等内容封装成结构化记录
def record_emotion(person, relation, event, emotion):
    today = datetime.date.today().isoformat()
    user_memory["emo_room"].append({
        "person": person,         # 涉及的对象（如女朋友）
        "relation": relation,     # 关系类型（如伴侣）
        "event": event,           # 事件描述（如加班争吵）
        "emotion": emotion,       # 当前情绪（如焦虑）
        "timestamp": today        # 时间戳（用于判断变化趋势）
    })

# 更新趋势函数：识别 emo_room 中情绪是否发生明显变化
def update_trends():
    if len(user_memory["emo_room"]) < 2:
        return
    # 取最后两条 emo 记录，因为我们要分析的是最近的情绪
    # 倒数第二条代表用户之前的情绪，倒数第一条代码用户现在的情绪，我们关注这两条就好
    # 其他数据可以做分析，不过现在对话模块只需要这两条即可
    # 我们把他们放在两个list分别是prev和latest
    prev, latest = user_memory["emo_room"][-2], user_memory["emo_room"][-1]
    if prev["emotion"] == "焦虑" and ("好" in latest["emotion"] or "改善" in latest["emotion"]):
        user_memory["trends"].append({
            "person": prev["person"],             # 关联对象
            "from": prev["emotion"],              # 起始情绪
            "to": latest["emotion"],              # 当前情绪
            "start": prev["timestamp"],           # 起始时间
            "end": latest["timestamp"],           # 当前时间
            "description": f"{prev['person']}的情绪由焦虑改善为积极"  # 趋势描述
        })

# -------------------------
# 模拟用户对话过程
# 第1轮输入：“我最近跟女朋友吵架了，她总是因为我加班而生气，我很焦虑”
record_emotion("女朋友", "伴侣", "因为加班争吵", "焦虑")

# 中间几轮略过...

# 第5轮输入：“女朋友理解我了，我现在好多了”
record_emotion("女朋友", "伴侣", "情绪有所缓和", "现在好多了")

# 更新趋势识别
update_trends()

# 打印结果（结构化 JSON）
print(json.dumps(user_memory, ensure_ascii=False, indent=2))
