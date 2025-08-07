
import argparse
from transformers import pipeline
import gradio as gr

def main(model_name):
    sentiment_analyzer = pipeline("sentiment-analysis", model=model_name)

    def analyze_sentiment(text):
        result = sentiment_analyzer(text)[0]
        return f"Label: {result['label']}, Score: {result['score']:.2f}"

    iface = gr.Interface(fn=analyze_sentiment, inputs="text", outputs="text")
    iface.launch()

if __name__ == "__main__":
    parser = argparse.ArgumentParser(description="Sentiment Analysis with configurable transformer model.")
    parser.add_argument('--model', type=str, default=None, help='HuggingFace model name to use for sentiment analysis')
    args = parser.parse_args()
    main(args.model)

