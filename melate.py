import numpy as np
import csv
import matplotlib.pyplot as plt
from re import sub
from decimal import Decimal


lines=[]
incluye=817

cont=0
with open("Melate.csv",'rb') as f:
    reader=csv.reader(f)
    for row in reader:
        if cont<incluye:
            cont+=1
            lines.append(row)
f.close()
lines.pop(0)

numeros=56
numberData=len(lines)



countNumber=np.zeros(56)
countNumberMatrix=np.zeros((7,numberData))
allData=np.zeros(numberData*7)

i=-1
for l in lines:
    i+=1
    for j in range(7):
        allData[i*7+j]=float(l[j+2])
        countNumber[float(l[j+2])-1]+=1;        
        countNumberMatrix[j,i]=float(l[2+j]) 



fig=plt.figure()
plt.hist(allData,range(1,numeros))
plt.savefig("histogramALLnumbers.pdf")
plt.close(fig)



for i in xrange(7):
    fig=plt.figure()
    plt.hist(countNumberMatrix[i,:],range(1,numeros))
    i2=i+1
    plt.savefig("%dhistogram.pdf" % i2)
    fig=plt.figure()
    plt.close(fig)


