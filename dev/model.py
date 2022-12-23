import pandas as pd
import numpy as np
import os
import joblib, dill
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier

currPath = os.path.join(os.getcwd())
dataPath = os.path.join(currPath, "dataset/Reduced Dataset CSV.csv")
modelStoragePath = currPath + "/modelStorage_url/"

if __name__ == "__main__":
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

    vectorizer = TfidfVectorizer(tokenizer=makeTokens)

    X = vectorizer.fit_transform(url_arr)

    
    X_train, X_test, y_train, y_test = train_test_split(X, y, random_state=42, test_size=0.2)

    RF = RandomForestClassifier(n_estimators=200, criterion='entropy', random_state=42)
    RF.fit(X_train, y_train)

    with open(modelStoragePath + "url_tokenizer.pkl", "wb") as fin0:
            dill.dump(makeTokens, fin0)
            print("Make tokens dumped")
    with open(modelStoragePath + "url_vectorizer.pkl", "wb") as fin1:
        joblib.dump(vectorizer, fin1)
        print("Vectorizer dumped")

    with open(modelStoragePath + "url_model.pkl", "wb") as fin2:
        joblib.dump(RF, fin2)
        print("Model dumped")
    print(RF.score(X_test, y_test))

    # joblib.dump(makeTokens, modelStoragePath + "makeTokens.pkl")
    # print("Make Tokens Dumped")

    #Dumping columns for validation
    # joblib.dump(dataset.columns.to_list(), modelStoragePath + "modelColumns.pkl")
    # print("Columns Dumped")
    query = vectorizer.transform(["https://www.google.co.in",
    "https://www.youtube.in",
    "facebook.unitedcolleges.net",
    "eyeappealoptometry.com/",
    "http://www.simmeurope.com/index.php?view=article&id=23:budget-economique-exploratoire-pour-lannee-2012&tmpl=component&print=1&layout=default&page=&option=com_content&Itemid=48",
    "http://spplodz.nazwa.pl/archiwum/2006_08b.php",
    "http://kickass.to",
    "https://www.bmst.ac.in",
    "https://vtu.ac.in",
    "https://github.com/arhamsc/Invigilation-System-BMSIT"])

    print(query)
    print(RF.predict(query))

    def predictUrl(url):
        X_predict = vectorizer.transform([url])
        return RF.predict(X_predict)