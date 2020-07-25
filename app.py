from flask import Flask, jsonify, request
import pandas as pd
import joblib
from sklearn.feature_extraction.text import CountVectorizer

app = Flask(__name__)

#Load the Spam
data = pd.read_csv('alt.csv')
X = data["Message_stop"]
count = CountVectorizer(min_df=5,ngram_range=[3,6],analyzer='char').fit(X)
spam_model = joblib.load('spam.pkl')


@app.route("/", methods=["POST"])
def home():
    #Check for spam
    req = request.get_json()
    msg = req["message"]
    yeet = count.transform(["Hi", "Lol"])
    print(spam_model.predict(yeet))