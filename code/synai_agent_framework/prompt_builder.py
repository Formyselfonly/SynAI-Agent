# 4. prompt_builder.py

def build_system_prompt(synai_room):
    style_pref = synai_room.preference_room['style_preferences']
    if style_pref:
        return f"你是一个温柔的心理AI，用户喜欢{style_pref[-1]['preference']}的风格"
    return "你是一个心理咨询AI"

def build_user_prompt(user_input, synai_room):
    if synai_room.emo_room:
        latest_event = synai_room.emo_room[-1]
        memory = f"# Memory: 用户在{latest_event['timestamp']}因为{latest_event['event']}感到{latest_event['emotion']}"
        return f"{user_input}\n{memory}"
    return user_input