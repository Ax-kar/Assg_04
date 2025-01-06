from transformers import pipeline
import gradio as gr

sentiment_analyzer = pipeline("sentiment-analysis")

def analyze_sentiment(text):
    result = sentiment_analyzer(text)[0]
    return f"Label: {result['label']}, Score: {result['score']:.2f}"

iface = gr.Interface(fn=analyze_sentiment, inputs="text", outputs="text")
iface.launch()
