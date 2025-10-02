import matplotlib.pyplot as plt 
import numpy as np 

def dgdx(x,y,g):
    return 4*y
def f(x):
    e=np.exp
    return 0.5*e(2*x)+0.5*e(-2*x)
   
x=0
y=1
dy=0
xf=10
n=1000
h=(xf-x)/(n-1)
xx,yy,yy1=[],[],[]
for i in range (n):
    dy=dy+h*dgdx(x,y,dy)
    y=y+dy*h
    y1=f(x)
    xx.append(x)
    yy.append(y)
    yy1.append(y1)
    x=x+h

plt.plot(xx,yy)
plt.plot(xx,yy1,':')
plt.show()