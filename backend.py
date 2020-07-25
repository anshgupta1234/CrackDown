from flask import Flask, jsonify, request

app = Flask()

@app.route("/", methods=["POST"])
def home():
    print("holder")