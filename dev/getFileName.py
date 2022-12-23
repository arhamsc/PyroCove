from pathlib import Path

cwd = Path(__file__).parent
pyroCoveDir = cwd.parent
dataPath_url = pyroCoveDir / "dev/dataset/Reduced Dataset CSV.csv"
dataPath_ip = pyroCoveDir / "dev/dataset/OnlyIPData.csv"
modalStoragePath_url = pyroCoveDir / "dev/modelStorage_url"
modalStoragePath_ip = pyroCoveDir / "dev/modelStorage_ip"

def getFilePath(fileName, type):
    if (type == "ip"):
        return modalStoragePath_ip / f"{fileName}.pkl"
    elif (type == "url"):
        return modalStoragePath_url / f"{fileName}.pkl"