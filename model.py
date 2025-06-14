from transformers import pipeline
from fastapi import HTTPException

try:
    classifier = pipeline("sentiment-analysis", model="distilbert-base-uncased")
except Exception as e:
    raise HTTPException(status_code=500, detail=str(e))

def predict_sentiment(text: str):
    result = classifier(text)
    return result[0]
