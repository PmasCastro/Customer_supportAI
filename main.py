import os
from typing import List
from dotenv import load_dotenv 
import openai
import gradio as gr


load_dotenv
openai_api_key = os.getenv('OPENAI_API_KEY')

system_message = "You are a helpful assistant"

def message_gpt(prompt):
    messages = [
        {"role": "assistant", "content": system_message},
        {"role": "user", "content": prompt}
    ]
    completion = openai.chat.completions.create(
        model="gpt-4o-mini",
        messages= messages,
    )
    return completion.choices[0].message.content

gr.Interface(fn=message_gpt, inputs="textbox", outputs="textbox", flagging_mode="never").launch(inbrowser=True)