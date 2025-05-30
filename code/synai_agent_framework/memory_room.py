from typing import List, Dict

class SynAIRoom:
    def __init__(self):
        self.emo_room: List[Dict] = []  # 情绪与人际关系信息
        self.preference_room: Dict[str, List[Dict]] = {
            "style_preferences": [],
            "language_preferences": [],
            "interaction_preferences": []
        }
        self.dialogue_room: List[str] = []  # 对话历史

    def add_dialogue(self, user_input: str):
        self.dialogue_room.append(user_input)