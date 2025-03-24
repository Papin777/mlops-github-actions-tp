def predict_sentiment(text):
    """
    Predict the sentiment of a given text.

    Args:
        text (str): Input text.

    Returns:
        str: Sentiment ("positive", "negative", "neutral")
    """
    if not text:
        return "neutral"
    if "happy" in text.lower() or "good" in text.lower():
        return "positive"
    if "sad" in text.lower() or "bad" in text.lower():
        return "negative"
    return "neutral"

