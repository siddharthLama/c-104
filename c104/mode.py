import csv
from collections import Counter

with open("weight.csv",newline ="")as f:
    reader = csv.reader(f)
    fileData = list(reader)
fileData.pop(0)
newData = []

for i in range(len(fileData)):
    num = fileData[i][2]
    newData.append(float(num))
# print(newData)

n = len(newData)

data = Counter(newData)
getMode = dict(data)

mode1 = []
mode2 = []
mode3 = []

for a,v in getMode.items():
    a = float(a)
    if 85 < a <110 :
        if v == max(list(data.values())):
            mode1.append(a)
    
    elif 110< a < 135 :
        if v == max(list(data.values())):
            mode2.append(a)

    elif 135< a <160 :
        if v == max(list(data.values())) :
            mode3.append(a)

if len(mode1)>len(mode2) and len(mode3) : 
    print(mode1)

elif len(mode2)> len(mode3) and len(mode1) :
    print(mode2)

elif len(mode3)> len(mode1) and len(mode2):
    print(mode3)