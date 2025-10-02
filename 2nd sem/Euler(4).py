import matplotlib.pyplot as plt
import numpy as np

def f(x,y):
    pi=np.pi
    x1=(-pi*y) 
    y1=(pi*x) 
    return x1,y1

ti=0
tf=4
x=1
y=0
n=10000
h=(tf-ti)/(n-1)
tt,xx,yy=[],[],[]
for i in range (n):
    t=ti+i*h
    x1,y1=f(x,y)
    y=y+h*y1
    x=x+h*x1
    
    yy.append(y)
    xx.append(x)
    tt.append(t)
fig,ax=plt.subplots(2,1,figsize=(8,8),constrained_layout=True)
ax[0].plot(tt,xx,'-.',color="red") 
ax[0].plot(tt,yy,'--',color="green") 
ax[0].axvline(x=0,color='Black')
ax[0].axhline(y=0,color='Black')
ax[0].grid(True)
ax[0].set_ylabel("y(t) or x(t)$\\rightarrow$")
ax[0].set_xlabel("time$\\rightarrow$")
ax[0].set_title("Plot of y(t) vs time & x(t) vs time")
                
ax[1].plot(xx,yy,'--',color="green") 
ax[1].axvline(x=0,color='Black')
ax[1].axhline(y=0,color='Black')
ax[1].grid(True)
ax[1].set_ylabel("y(t)$\\rightarrow$")
ax[1].set_xlabel("x(t)$\\rightarrow$")
ax[1].set_title("Plot of y(t) vs x(t)")
plt.show()
