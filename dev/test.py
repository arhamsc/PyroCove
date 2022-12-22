import pandas as pd
import numpy as np
import os
import joblib

currPath = os.path.join(os.getcwd(), "dev")
dataPath = os.path.join(currPath, "dataset/Reduced Dataset CSV.csv")

dataset = pd.read_csv(dataPath)

url_arr = dataset["url"]
y = dataset["type"]

print(dataset.columns.to_list())