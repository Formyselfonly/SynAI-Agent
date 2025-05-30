from extractor import extract_keywords_and_emotions

def update_memory(synai_room, user_input: str):
    info = extract_keywords_and_emotions(user_input)
    synai_room.emo_room.append(info)
    synai_room.add_dialogue(user_input)