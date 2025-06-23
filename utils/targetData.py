import os
import json

if not os.path.exists("targetsData.json"):
    with open("targetsData.json", "w") as file:
        json.dump({}, file)        
        
def isTargetDataExist(targetUsername):
    with open("targetsData.json", "r") as file:
        data = json.load(file)
    if targetUsername in data:
        return True
    else:
        return False
    
def getTargetData(targetUsername):
    with open("targetsData.json", "r") as file:
        data = json.load(file)
    if targetUsername in data:
        return data[targetUsername]
    else:
        return None

def setTargetData(targetUsername, targetData):
    with open("targetsData.json", "r") as file:
        data = json.load(file)
    data[targetUsername] = targetData
    with open("targetsData.json", "w") as file:
        json.dump(data, file)
        