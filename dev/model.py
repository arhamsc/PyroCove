import pandas as pd
import numpy as np
import os
import joblib

currPath = os.path.join(os.getcwd())
dataPath = os.path.join(currPath, "dataset/Reduced Dataset CSV.csv")
modelStoragePath = currPath + "/modelStorage/"

dataset = pd.read_csv(dataPath)

url_arr = dataset["url"]
y = dataset["type"]

def makeTokens(f):
    tkns_BySlash = str(f.encode('utf-8')).split('/')
    total_Tokens = []

    for i in tkns_BySlash:
        tokens = str(i).split('-')
        tkns_ByDot = []

    for j in range(0,len(tokens)):
        temp_Tokens = str(tokens[j]).split('.')
        tkns_ByDot = tkns_ByDot + temp_Tokens
        total_Tokens = total_Tokens + tokens + tkns_ByDot
    total_Tokens = list(set(total_Tokens))

    if 'com' in total_Tokens:
        total_Tokens.remove('com')
 
    return total_Tokens

with open(modelStoragePath + "tokenizer.pkl", "wb") as fin:
    joblib.dump(makeTokens, fin)

from sklearn.feature_extraction.text import TfidfVectorizer
vectorizer = TfidfVectorizer(tokenizer=makeTokens)

with open(modelStoragePath + "vectorizer.pkl", "wb") as fin:
    joblib.dump(vectorizer, fin)

X = vectorizer.fit_transform(url_arr)

if __name__ == "__main__":
    from sklearn.model_selection import train_test_split
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42, test_size=0.2)

    from sklearn.ensemble import RandomForestClassifier

    RF = RandomForestClassifier(n_estimators=200, criterion='entropy', random_state=42)
    RF.fit(X_train, y_train)

    joblib.dump(RF, modelStoragePath + "model.pkl")
    print("Model dumped")

    joblib.dump(makeTokens, modelStoragePath + "makeTokens.pkl")
    print("Make Tokens Dumped")

    #Dumping columns for validation
    joblib.dump(dataset.columns.to_list(), modelStoragePath + "modelColumns.pkl")
    print("Columns Dumped")

    def predictUrl(url):
        X_predict = vectorizer.transform([url])
        return RF.predict(X_predict)