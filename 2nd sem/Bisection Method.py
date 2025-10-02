import matplotlib.pyplot as plt
import numpy as np

def f(x):
    return np.exp(-x)*(3.2*np.sin(x)-0.5*np.cos(x))

def fn(a,b,h,n):
    xx,yy=[],[]
    for i in range (n):
        x=a+i*h
        y=f(x)
        xx.append(x)
        yy.append(y)
    return xx,yy    
a=0
b=6
xi=3
xf=4
n=1000
h=(b-a)/(n-1)
xx,yy=fn(a,b,h,n)
d=10**(-5)
while abs(xf-xi)>=d:
    if f(xi)*f(xf)<0:
        c=(xf+xi)/2
        if f(c)*f(xf)<0:
            xi=c
        elif f(c)*f(xf)>0:
            xf=c  

plt.scatter(c,f(c))
plt.text(c, f(c)+0.04, f"{c:.3f},{f(c):.3f}")
plt.plot(xx,yy,color="red")  
plt.axvline(x=0,color='Black')
plt.axhline(y=0,color='Black')
plt.grid(True)
plt.title("root of a function: $e^{-x} \\left( 3.2\\sin{(x)}-0.5\\cos{(x)} \\right) $")
plt.ylabel("y(x)$\\rightarrow$")
plt.xlabel("x$\\rightarrow$")
plt.show()
