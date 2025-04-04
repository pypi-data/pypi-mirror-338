from transformers import pipeline

sentiment_pipeline = pipeline("sentiment-analysis", model="cardiffnlp/twitter-roberta-base-sentiment")

def analyze_sentiment(text):
    result = sentiment_pipeline(text)[0]
    label = result["label"]
    confidence = result["score"]

    if label == "LABEL_0":  
        sentiment = "NEGATIVE"
    elif label == "LABEL_1":  
        sentiment = "NEUTRAL"
    elif label == "LABEL_2": 
        sentiment = "POSITIVE"
    
    return {"sentiment": sentiment, "confidence": confidence}

print(analyze_sentiment("I'm not sure how I feel about this.")) 
