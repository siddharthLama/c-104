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
mode4 = []
mode5 = []
mode6 = []
mode7 = []
mode8 = []
mode9 = []
mode10 = []


for a,v in getMode.items():
    a = float(a)
    if 75 < a <85 :
        if v == max(list(data.values())):
            mode1.append(a)

    elif 85 < a <95 :
        if v == max(list(data.values())):
            mode2.append(a)
            

    elif 95 < a <105 :
        if v == max(list(data.values())):
            mode3.append(a)

    elif 105 < a <115 :
        if v == max(list(data.values())):
            mode4.append(a)

    elif 115 < a <125 :
        if v == max(list(data.values())):
            mode5.append(a)

    elif 125 < a <135 :
        if v == max(list(data.values())):
            mode6.append(a)

    elif 135 < a <145 :
        if v == max(list(data.values())):
            mode7.append(a)

    elif 145 < a <155 :
        if v == max(list(data.values())):
            mode8.append(a)
    
    elif 155< a < 165 :
        if v == max(list(data.values())):
            mode9.append(a)

    elif 165< a <175 :
        if v == max(list(data.values())) :
            mode10.append(a)

if len(mode1) > len(mode2) and len(mode3) and len(mode4) and len(mode5) and len(mode6) and len(mode7) and len(mode8) and len(mode9) and len(mode10) : 
    print(mode1)

elif len(mode2)> len(mode3) and len(mode1) and len(mode4) and len(mode5) and len(mode6) and len(mode7) and len(mode8) and len(mode9) and len(mode10):
    print(mode2)

elif len(mode3)> len(mode1) and len(mode2) and len(mode4) and len(mode5) and len(mode6) and len(mode7) and len(mode8) and len(mode9) and len(mode10):
    print(mode3)

elif len(mode4)> len(mode1) and len(mode2) and len(mode3) and len(mode5) and len(mode6) and len(mode7) and len(mode8) and len(mode9) and len(mode10):
    print(mode4)

elif len(mode5)> len(mode1) and len(mode2) and len(mode3) and len(mode4) and len(mode6) and len(mode7) and len(mode8) and len(mode9) and len(mode10):
    print(mode5)

elif len(mode6)> len(mode1) and len(mode2) and len(mode3) and len(mode4) and len(mode5) and len(mode7) and len(mode8) and len(mode9) and len(mode10):
    print(mode6)

elif len(mode7)> len(mode1) and len(mode2) and len(mode3) and len(mode4) and len(mode5) and len(mode6) and len(mode8) and len(mode9) and len(mode10):
    print(mode7)

elif len(mode8)> len(mode1) and len(mode2) and len(mode3) and len(mode4) and len(mode5) and len(mode6) and len(mode7) and len(mode9) and len(mode10):
    print(mode8)

elif len(mode9)> len(mode1) and len(mode2) and len(mode3) and len(mode4) and len(mode5) and len(mode6) and len(mode7) and len(mode8) and len(mode10):
    print(mode9)

elif len(mode10)> len(mode1) and len(mode2) and len(mode3) and len(mode4) and len(mode5) and len(mode6) and len(mode7) and len(mode8) and len(mode9):
    print(mode10)
