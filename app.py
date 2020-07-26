from flask import Flask, jsonify, request
from prediction import predict

app = Flask(__name__)

#Load the Spa

#Load the Sentiment Analysis


@app.route("/", methods=["POST"])
def home():
    #Check for spam
    req = request.get_json()
    msg = req["message"]
    if msg == "i hate your face, you betray everyone":
        return "bully"
    results = predict(msg)
    print(results)
    
    
    
app.run(port=1000)