from transformers import AutoModelForSequenceClassification, AutoTokenizer
import torch

# Load model and tokenizer manually
MODEL_NAME = "distilbert/distilbert-base-uncased-finetuned-sst-2-english"
tokenizer = AutoTokenizer.from_pretrained(MODEL_NAME)
model = AutoModelForSequenceClassification.from_pretrained(MODEL_NAME)

def analyze_sentiment(text: str) -> dict:
    """Analyze sentiment using a pre-trained transformer model."""
    inputs = tokenizer(text, return_tensors="pt", truncation=True, padding=True)
    outputs = model(**inputs)
    scores = torch.nn.functional.softmax(outputs.logits, dim=-1)

    # Convert scores to readable labels
    labels = ["NEGATIVE", "POSITIVE"]
    confidence, label = torch.max(scores, dim=1)
    
    return {
        "sentiment": labels[label.item()],
        "confidence": confidence.item()
    }
