from transformers import pipeline

# Load sentiment analysis model (ensure it's a 3-class model)
sentiment_pipeline = pipeline("sentiment-analysis", model="cardiffnlp/twitter-roberta-base-sentiment")

def analyze_sentiment(text):
    result = sentiment_pipeline(text)[0]
    label = result["label"]
    confidence = result["score"]

    # Adjusting sentiment classification based on confidence scores
    if label == "LABEL_0":  # Negative
        sentiment = "NEGATIVE"
    elif label == "LABEL_1":  # Neutral
        sentiment = "NEUTRAL"
    elif label == "LABEL_2":  # Positive
        sentiment = "POSITIVE"
    
    return {"sentiment": sentiment, "confidence": confidence}

# Test the fix
print(analyze_sentiment("I'm not sure how I feel about this."))  # Expected: NEUTRAL
