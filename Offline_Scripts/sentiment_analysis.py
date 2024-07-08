# Install necessary packages
# !pip install transformers torch

from transformers import pipeline

# Initialize the sentiment analysis pipeline
sentiment_analyzer = pipeline("sentiment-analysis")

def analyze_sentiment(text):
    """
    Analyzes the sentiment of the given text.
    
    Args:
        text (str): The text to analyze.
    
    Returns:
        dict: The sentiment analysis result.
    """
    return sentiment_analyzer(text)[0]

if __name__ == "__main__":
    # Example text
    text = "I love using open-source AI models. They make life so much easier!"
    
    # Analyze sentiment
    result = analyze_sentiment(text)
    
    # Print the result
    print(f"Text: {text}")
    print(f"Sentiment: {result['label']}")
    print(f"Confidence Score: {result['score']:.4f}")
