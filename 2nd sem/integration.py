import numpy as np
def f(x):
    y1=np.sin(x)
    y2=np.cos(x)
    if y1>=y2:
        return y2
    else: 
        return y1
yy=[]
xi=0
xf=np.pi/2
n=1000
s=0
h=(xf-xi)/(n-1)
for i in range(0,n):
    x=xi+i*h
    y=f(x) 
    yy.append(y)     
for i in range(1,n-1):
    s=s+2*yy[i]
s=s+yy[0]+yy[n-1]   
m=s*h/2 
m=round(m,5)
print(m)
