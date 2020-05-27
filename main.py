import requests
import json
import os

base = (json.loads(requests.get("https://api.exchangeratesapi.io/latest?base=USD").text))

def createString(csvArr):
    fnlStr = ""
    for i,el in enumerate(csvArr):
        fnlStr += str(el)
        if i != len(csvArr) - 1:
            fnlStr += ","
        else:
            fnlStr += "\n"
    return fnlStr

for b in base['rates']:
    csvarrs = ([base['date'], b, base['rates'][b]])
    if not os.path.isdir("data/"+b):
        os.mkdir("data/"+b)
    filename = "data/"+b+"/rate.csv"

    if not os.path.isfile(filename) and not os.access(filename, os.R_OK):
        pf = open(filename, "w")
    if os.stat(filename).st_size == 0:
        WriteData = open(filename, "a")
        WriteData.write("date, base, rates")
        WriteData.close()
    WriteData = open(filename, "a")
    WriteData.write(createString(csvarrs))
    WriteData.close()

