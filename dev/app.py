from flask import Flask, request, jsonify
import joblib
import traceback
import sys
import pandas as pd
import numpy as np

#Equivalent to app = Express()
app = Flask(__name__)

vectorizer = ""
makeTokens = ""
with open("/Volumes/Arham/A2/BMS College stufff/PBL/5th Sem PBl/PyroCove/dev/modelStorage/tokenizer.pkl", "rb") as fin:
    makeTokens = joblib.load(fin)
with open("/Volumes/Arham/A2/BMS College stufff/PBL/5th Sem PBl/PyroCove/dev/modelStorage/vectorizer.pkl", "rb") as fin:
    vectorizer = joblib.load(fin)

try:
    port = int(sys.argv[1])
except:
    port = 3500

RF = joblib.load("/Volumes/Arham/A2/BMS College stufff/PBL/5th Sem PBl/PyroCove/dev/modelStorage/model.pkl")
print("Model Loaded")

# vectorizer = joblib.load("/Volumes/Arham/A2/BMS College stufff/PBL/5th Sem PBl/PyroCove/dev/modelStorage/vectorizer.pkl")
# print("Vectorizer loaded")

model_columns = joblib.load("/Volumes/Arham/A2/BMS College stufff/PBL/5th Sem PBl/PyroCove/dev/modelStorage/modelColumns.pkl")
print("Model Columns loaded")

# if __name__ == '__main__':
#     try:
#         port = int(sys.argv[1])
#     except:
#         port = 3500
    
#     RF = joblib.load("/Volumes/Arham/A2/BMS College stufff/PBL/5th Sem PBl/PyroCove/dev/modelStorage/model.pkl")
#     print(RF)
#     print("Model Loaded")
#     model_columns = joblib.load("/Volumes/Arham/A2/BMS College stufff/PBL/5th Sem PBl/PyroCove/dev/modelStorage/modelColumns.pkl")
#     print("Model Columns loaded")

def transformResponse(predictionArray, originalUrls):
    return {
        originalUrls: predictionArray
    }


@app.route('/predict', methods=['POST'])
def predict():
    if RF:
        try:
            json_ = request.json
            # query = pd.get_dummies(pd.DataFrame(json_))
            # query = query.reindex(columns=model_columns, fill_value=0)
            query = vectorizer.transform(json_["urls"])
            prediction = list(RF.predict(query))
            response = list(map(transformResponse, prediction, json_["urls"]))
            print(response)
            return jsonify({'prediction': response})
        except:
            return jsonify({'trace': traceback.format_exc()})
    else:
        print("Train the model first")
        return("No model here to use.")

if __name__ == "__main__":
    app.run(debug=True, port=3500)