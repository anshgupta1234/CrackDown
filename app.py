from flask import Flask, jsonify, request
from flask_cors import CORS
import pandas as pd
import joblib
from sklearn.feature_extraction.text import CountVectorizer
from  sklearn.model_selection import train_test_split
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from prediction import predict

app = Flask(__name__)

#Load the Spa

#Load the Sentiment Analysis


@app.route("/", methods=["POST"])
def home():
    #Check for spam
    req = request.get_json()
    msg = req["message"]
    results = predict(msg)
    print(results)
    return results
    
    
app.run(port=1000)