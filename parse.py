import csv
import sys
from pathlib import Path

number=sys.argv[1]
filename=sys.argv[2]

def vendor2list(data):
    result=[]
    with open(data,'r',encoding='latin-1') as file:
        for line in file:
            line=line.split('|')
            line=line[2:-1] 
            result.append(line)
    return result

list_=(vendor2list(filename))
result=[]
for i in list_:
    if i[2]==str(number):
        result.append(i)
length=[]        
for i in result:
    length.append(len(i))
cols=min(length)
for i in range(len(result)):
    if len(result[i])>cols:
        result[i]=result[i][0:cols-len(result[i])] 
with open(Path(filename).stem+'_'+str(number)+'.csv','w') as file:
    file=csv.writer(file)
    for i in result:
        file.writerow(i)
print(Path(filename).stem)