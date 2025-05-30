import datetime
import re

# 模拟关系词典，可后续扩展
RELATION_MAP = {
    "女朋友": "伴侣",
    "男朋友": "伴侣",
    "妈妈": "母亲",
    "爸爸": "父亲",
    "导师": "学术指导",
    "朋友": "朋友"
}

# 模拟情绪词典
EMOTION_LIST = ["焦虑", "沮丧", "开心", "崩溃", "压力大", "失落", "紧张", "生气", "愧疚", "绝望"]

def extract_keywords_and_emotions(user_input: str):
    today = datetime.date.today().isoformat()
    result = {
        "emo_room": [],
        "dialogue_room": [user_input]
    }

    # 抽取人名 + 关系
    found_person = None
    for key in RELATION_MAP:
        if key in user_input:
            found_person = key
            break

    # 抽取情绪
    found_emotion = None
    for emo in EMOTION_LIST:
        if emo in user_input:
            found_emotion = emo
            break

    # 抽取事件（可拓展成事件识别模块，这里简化为句子截断）
    # 找到“因为xxx”，“由于xxx”
    match = re.search(r"(因为|由于)([^，。！!]+)", user_input)
    event = match.group(0) if match else "未提及具体事件"

    memory_item = {
        "person": found_person if found_person else "自我",
        "relation": RELATION_MAP.get(found_person, "用户本人"),
        "event": event,
        "emotion": found_emotion if found_emotion else "未识别",
        "timestamp": today
    }

    result["emo_room"].append(memory_item)
    return result
