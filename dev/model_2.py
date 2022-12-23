import pandas as pd
import numpy as np
import os
import joblib
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
import dill


currPath = os.path.join(os.getcwd())
dataPath = os.path.join(currPath, "dataset/OnlyIPData.csv")
modelStoragePath = currPath + "/modelStorage_ip/"

if __name__ == "__main__":
    dataset = pd.read_csv(dataPath)

    url_arr = dataset["IP"]
    y = dataset["Type"]

    def makeTokens(f):
        tokens = str(f.encode('utf-8')).split('.')
        total_Tokens = []

        for _ in range(0,len(tokens)):
            total_Tokens = total_Tokens + tokens
        total_Tokens = list(set(total_Tokens))

        return total_Tokens

    vectorizer = TfidfVectorizer(tokenizer=makeTokens)

    X = vectorizer.fit_transform(url_arr)

    
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42, test_size=0.2)

    from sklearn.ensemble import RandomForestClassifier

    RF = RandomForestClassifier(n_estimators=200, criterion='entropy', random_state=42)
    RF.fit(X_train, y_train)
    print(RF.score(X_test, y_test))

    with open(modelStoragePath + "ip_tokenizer.pkl", "wb") as fin:
        dill.dump(makeTokens, fin)
        print("Make Tokens dumped.")

    with open(modelStoragePath + "ip_vectorizer.pkl", "wb") as fin:
        joblib.dump(vectorizer, fin)
        print("Vectorizer dumped")

    with open(modelStoragePath + "ip_model.pkl", "wb") as fin:
        joblib.dump(RF, fin)
        print("Model dumped")

    def predictUrl(ip):
        X_predict = vectorizer.transform([ip])
        return RF.predict(X_predict)
    print(predictUrl("192.168.2.1"))
    print(predictUrl("189.174.22.222"))