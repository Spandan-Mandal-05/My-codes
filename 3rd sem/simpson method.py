import numpy as np
import matplotlib.pyplot as plt

def fx(r):
    xi=x=0
    xf=3
    n=10**3+1
    h=(xf-xi)/(n-1)
    def f(x,r):
        return x**r
    g=0
    m=0
    yy=[]
    for k in range (0,n):
        y=f(x,r)
        yy.append(y)
        x += h
    for j in range (0,n//2):
        g=g+4*yy[2*j+1]
        if 2*j+2 < (n-1):
            m=m+2*yy[2*j+2]
    s=h/3*(yy[0]+g+m+yy[n-1])
    return s 

xx=np.linspace(0,4,10**2)
y1=[fx(r) for r in xx ]

plt.plot(xx,y1)
plt.show()


    