import matplotlib.pyplot as plt
import numpy as np

def f(x,y): #define the ODE 
    y1=np.exp(-x)-2*y
    y2=np.exp(-x)-np.exp(-2*x)
    return y1,y2

xi=0
xf=5
y=0
n=500
h=(xf-xi)/(n-1)
xx,yy1,yy2=[],[],[]
for i in range (n):
    y1,y2=f(xi,y)
    y=y+h*y1
    yy1.append(y)
    yy2.append(y2)
    xx.append(xi)
    xi=xi+h

plt.plot(xx,yy1,'-.',label='Plot of ODE',color="red") 
plt.plot(xx,yy2,'--',label="real sol.",color="green") 
plt.axvline(x=0,color='Black')
plt.axhline(y=0,color='Black')
plt.grid(True)
plt.title(" Solving ODE: $ \\frac{dy}{dx} + 2y-e^{{-x}} = 0 $")
plt.ylabel("y(x)$\\rightarrow$")
plt.xlabel("x$\\rightarrow$")
plt.legend(loc='best',fontsize=10)
plt.show()
