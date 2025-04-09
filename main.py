import os
from typing import List
from dotenv import load_dotenv 
import ollama
import openai
import gradio as gr

load_dotenv()
openai_api_key = os.getenv('OPENAI_API_KEY')

system_message = "You are an helpful AI assistant"

# def stream_gpt(prompt):
#     messages = [
#         {"role": "system", "content": system_message},
#         {"role": "user", "content": prompt}
#     ]
#     stream = openai.chat.completions.create(
#         model="gpt-4o-mini",
#         messages=messages,
#         stream=True,
#     )
#     result = ""
#     for chunk in stream:
#         result += chunk.choices[0].delta.content or ""
#         yield result


def get_ollama(prompt):
    messages = [
        {"role": "system", "content": system_message},
        {"role": "user", "content": prompt},
    ]
    response = ollama.chat(
        messages=messages,
        model="llama3.2",
        )
    return response['message']['content']

view = gr.Interface(
    fn = get_ollama,
    inputs=[gr.Textbox(label="Your message:")],
    outputs=[gr.Markdown(label="Response:")],
    flagging_mode="never"
)
view.launch()