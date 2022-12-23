import joblib
from pathlib import Path
from scapy.all import sniff, IP
import dill

cwd = Path(__file__).parent
pyroCoveDir = cwd.parent
modalStoragePath = pyroCoveDir / "dev/modelStorage_ip"

def getFilePath(fileName):
    return modalStoragePath / f"{fileName}.pkl"

makeTokens = (lambda x: x + x) #To initialize callable object for vectorizer

print(getFilePath("ip_tokenizer"))
try:
    with open(getFilePath("ip_model"), "rb") as fin:
        RF = joblib.load(fin)
        print("RF model loaded.")

    with open(getFilePath("ip_tokenizer"), "rb") as fin1:
        makeTokens = dill.load(fin1)
        print("Make Tokens loaded.")

    with open(getFilePath("ip_vectorizer"), "rb") as fin2:
        vectorizer = joblib.load(fin2)
        print("Vectorizer Loaded")
except FileNotFoundError as file:
    print(f"{file.filename} doesn't exist.")

def vectorizeInput(ipAddr):
    return vectorizer.transform([ipAddr])

def firewall(pkt):
    if IP in pkt:
        srcAddr = pkt[IP].src
        dstAddr = pkt[IP].dst
        print("Source:", srcAddr, "\tDestination:", dstAddr)
        predictSrc = vectorizeInput(srcAddr)
        predictedSrc = RF.predict(predictSrc)
        print("Predicted: ", predictedSrc)
        if (predictedSrc != ["good"]):
            pkt = None
            print(f"Packet with source: {srcAddr} - Dropped")

if __name__ == "__main__":
    print(makeTokens("192.123.233.232"))
    filter = "tcp"
    sniff(filter=filter, prn=firewall)