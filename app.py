from flask import Flask, jsonify, request
from flask_cors import CORS
import pandas as pd
import joblib
from sklearn.feature_extraction.text import CountVectorizer
from  sklearn.model_selection import train_test_split

app = Flask(__name__)

#Load the Spam
data = pd.read_csv('alt.csv')
X = data["Message_stop"]
y = data["Tag"]
X_train,X_test,y_train,y_test=train_test_split(X,y,random_state=0)
count = CountVectorizer(min_df=5,ngram_range=[3,6],analyzer='char').fit(X_train)
spam_model = joblib.load('spam.pkl')

@app.route("/", methods=["POST"])
def home():
    #Check for spam
    req = request.get_json()
    msg = req["message"]
    yeet = count.transform([msg])
    results = spam_model.predict(yeet)
    return { "spam": int(results[0]) }

app.run(port=1000)