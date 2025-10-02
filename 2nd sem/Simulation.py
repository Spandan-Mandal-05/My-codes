import matplotlib.pyplot as plt
import numpy as np


n=10*4
nn=[]
for i in range (n):
    n=np.random.rand()
    nn.append(n)
xx=np.arange(0,1,0.1)
yy=np.zeros(len(xx))
for j in xx:
    for x in nn:
        if j<=x<j+1/len(xx):
            yy[int(j*len(xx))]=yy[int(j*len(xx))]+1

toss=[]
n=1000
for k in range (n):
    y= np.random.choice(nn) 
    if 0<=y<0.5: toss.append("Head")
    elif 0.5<=y<1: toss.append("Tail")
    else: toss.append("None")
"""
xx,yy=[],[] 
for i in np.arange(0,1,0.001):
    xx.append(i)
    k=0
    n=10**3
    for j in range(n):
        x=np.random.rand()
        if i<=x<i+0.1:
            k+=1
    yy.append(k)"""
print(f"Tails = {toss.count("Head")}",f"Heads = {toss.count("Tail")}",f"None of them = {toss.count("None")}")        
plt.bar(np.arange(0,len(xx),1),yy)
plt.show()