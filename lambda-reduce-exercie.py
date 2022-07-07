import csv
import json
from functools import reduce

callsFile = open('calls.csv', 'r')
CF = csv.DictReader(callsFile)

filteredList = list(filter(lambda row : row["zip_code"] != "" and row["neighborhood"] != "" and row["totalresponsetime"] != "" and row["dispatchtime"] != "" and row["totaltime"] != "", CF))

trt = reduce(lambda trt1, dict : trt1 + float(dict["totalresponsetime"]), filteredList, 0)
avgtrt = (trt/len(filteredList))
print(avgtrt)

dpt = reduce(lambda dpt1, dict : dpt1 + float(dict["dispatchtime"]), filteredList, 0)
avgdpt = (dpt/len(filteredList))
print(avgdpt)

tt = reduce(lambda tt, dict : tt + float(dict["totaltime"]), filteredList, 0)
avgtt = (tt/len(filteredList))
print(avgtt)

Neighborhoods = []

for i in filteredList:
    if i["neighborhood"] not in Neighborhoods:
        Neighborhoods.append(i["neighborhood"])

jsonList = []

for i in Neighborhoods:
    nbd = list(filter(lambda row : row["neighborhood"] == i, filteredList))

ntrt = reduce(lambda ntrt1, dict : ntrt1 + float(dict["totalresponsetime"]), nbd, 0)
avgntrt = (ntrt/len(nbd))
print(avgntrt)

ndpt = reduce(lambda ndpt1, dict : ndpt1 + float(dict["dispatchtime"]), nbd, 0 )
avgndpt = (ndpt/len(nbd))
print(avgndpt)

ntt = reduce(lambda ntt1, dict : ntt1 + float(dict["totaltime"]), nbd, 0)
avgntt = ntt/len(nbd)
print(avgntt)

jsonList.append({"Neighborhoods": Neighborhoods, "avgtrt": avgntrt, 
                "avgdpt": avgndpt, "avgtt": avgntt})

jsonList.append({"Neighborhoods": "Overall", "avgtrt": avgntrt, 
                "avgdpt": avgndpt, "avgtt": avgntt})

with open("calls.json", "w") as outfile:
    json.dump(jsonList, outfile)
