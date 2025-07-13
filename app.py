import gradio as gr
from transformers import pipeline

chat = pipeline("text-generation", model="distilgpt2")

def bot(vuoropuhelu):
    prompt = "Asiakas: " + vuoropuhelu + "\nBotti:"
    vastaukset = chat(prompt, max_new_tokens=100, do_sample=True)
    return vastaukset[0]["generated_text"].split("Botti:")[-1].strip()

demo = gr.ChatInterface(fn=bot, title="IT-palvelubotti")

demo.launch()
