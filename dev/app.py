from flask import Flask, request, jsonify
from flask_cors import cross_origin
import joblib, dill
import traceback
import sys
import pandas as pd
import numpy as np
from pathlib import Path
from getFileName import getFilePath

#Equivalent to app = Express()
app = Flask(__name__)

makeTokens = (lambda x: x + x)
makeTokens_ip = (lambda x: x + x)

try:
    with open(getFilePath("url_model", "url"), "rb") as fin:
        RF = joblib.load(fin)
        print("RF model loaded.")
    
    with open(getFilePath("ip_model", "ip"),"rb") as fin:
        RF_IP = joblib.load(fin)

    with open(getFilePath("url_tokenizer", "url"), "rb") as fin1:
        makeTokens = dill.load(fin1)
        print("Make Tokens loaded.")

    with open(getFilePath("url_vectorizer", "url"), "rb") as fin2:
        vectorizer = joblib.load(fin2)
        print("Vectorizer Loaded.")

    with open(getFilePath("ip_tokenizer", "ip"), "rb") as fin1:
        makeTokens_ip = dill.load(fin1)
        print("Make Tokens loaded.")

    with open(getFilePath("ip_vectorizer", "ip"), "rb") as fin2:
        vectorizer_ip = joblib.load(fin2)
        print("Vectorizer Loaded.")
except FileNotFoundError as file:
    print(f"{file.filename} doesn't exist.")

def transformResponse(predictionArray, originalUrls):
    return {
        originalUrls: predictionArray
    }


@app.route('/predict/url', methods=['POST'])
@cross_origin()
def predict():
    if RF:
        try:
            json_ = request.json
            query = vectorizer.transform(json_["urls"])
            print(query)
            prediction = list(RF.predict(query))
            response = list(map(transformResponse, prediction, json_["urls"]))
            print(response)
            return jsonify({'prediction': response})
        except:
            return jsonify({'trace': traceback.format_exc()})
    else:
        print("Train the model first")
        return("No model here to use.")

@app.route('/predict/ip', methods=['POST'])
@cross_origin()
def predict_ip():
    if RF_IP:
        try:
            json_ = request.json
            query = vectorizer_ip.transform(json_["ips"])
            prediction = list(RF_IP.predict(query))
            response = list(map(transformResponse, prediction, json_["ips"]))
            print(response)
            return jsonify({'prediction': response})
        except:
            return jsonify({'trace': traceback.format_exc()})
    else:
        print("Train the model first")
        return("No model here to use.")

if __name__ == "__main__":
    app.run(debug=True, port=3500)