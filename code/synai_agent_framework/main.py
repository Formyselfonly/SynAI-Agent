
from fastapi import FastAPI
from memory_room import SynAIRoom
from memory_update import update_memory
from prompt_builder import build_system_prompt, build_user_prompt
import openai

app = FastAPI()
room = SynAIRoom()

@app.post("/chat")
def chat_with_memory(user_input: str):
    update_memory(room, user_input)
    system_prompt = build_system_prompt(room)
    user_prompt = build_user_prompt(user_input, room)

    response = openai.ChatCompletion.create(
        model="gpt-4",
        messages=[
            {"role": "system", "content": system_prompt},
            {"role": "user", "content": user_prompt}
        ]
    )
    return response['choices'][0]['message']['content']