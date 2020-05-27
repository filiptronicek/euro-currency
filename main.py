import requests
import json
import os

base = (json.loads(requests.get("https://api.exchangeratesapi.io/latest?base=USD").text))

print(base)

csvarrs = []

for b in base['rates']:
    csvarrs.append([base['date'], b, base['rates'][b]])
    if not os.path.isdir("data/"+b):
        os.mkdir("data/"+b)
    filename = "data/"+b+"/rate.csv"
    WriteData = open(filename, "a")
    WriteData.write(createString(csvarrs))
    WriteData.close()

def createString(csvArr):
    fnlStr = ""
    for i,el in enumerate(csvArr):
        fnlStr += str(el)
        if i != len(csvArr) - 1:
            fnlStr += ","
        else:
            fnlStr += "\n"
    return fnlStr