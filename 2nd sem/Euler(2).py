import matplotlib.pyplot as plt
import numpy as np

def f(x,y):
    e=np.exp
    y1=1-y**2  # given ODE
    y2=(e(2*x)-1)/(e(2*x)+1) # known solution of ODE
    return y1,y2

xi=0
xf=3
y=0
n=10000
h=(xf-xi)/(n-1)
xx,yy1,yy2=[],[],[]
for i in range (n):
    x=xi+i*h
    y1,y2=f(x,y)
    y=y+h*y1
    yy1.append(y)
    yy2.append(y2)
    xx.append(x)

plt.plot(xx,yy1,'-.',label='Plot of ODE',color="red") 
plt.plot(xx,yy2,'--',label="real sol.",color="green") 
plt.axvline(x=0,color='Black')
plt.axhline(y=0,color='Black')
plt.grid(True)
plt.title("solve ODE")
plt.ylabel("y(x)$\\rightarrow$")
plt.xlabel("x$\\rightarrow$")
plt.legend(loc='best',fontsize=10)
plt.show()
