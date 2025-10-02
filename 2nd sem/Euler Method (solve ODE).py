# dy/dx = x² + y

import numpy as np
import matplotlib.pyplot as plt
x=1
xf=5
y=1
n=501
h=(xf-x)/(n-1)
xx,y1,y2=[],[],[]
x1,y1=[],[]
for i in range (n):
    s=(x**2 + y) # put the equation
    y = y+h*s
    z=-(x**2+2*x+2)+6*np.exp(x-1) # solved ODE by hand 
    x=x+h
    xx.append(x)
    y1.append(y)
    y2.append(z)
    #print(x,y)

plt.plot(xx,y1,'-.',label='Plot of ODE',color="red") 
plt.plot(xx,y2,'--',label="real sol.",color="green") 
plt.axvline(x=0,color='Black')
plt.axhline(y=0,color='Black')
plt.grid(True)
plt.title("solve ODE")
plt.ylabel("y(x)$\\rightarrow$")
plt.xlabel("x$\\rightarrow$")
plt.legend(loc='best',fontsize=20)
plt.ylim(0,150)
plt.show()
