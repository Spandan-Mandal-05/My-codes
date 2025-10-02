import numpy as np
import matplotlib.pyplot as plt
x1=-2
x2=4
n=2
m=50
h=(x2-x1)/(m-1)
xx,y1,y2=[],[],[]
for i in range (m+1):
    x=x1+h*i
    y=np.exp(x)
    xx.append(x)
    y1.append(y)
    s=1
    k=0
    fact=1
    for j in range(1,n+1):
        fact=fact*j
        s=s+x**j/fact
    y2.append(s)

plt.plot(xx,y1,'-',label="exp(x)",color='b')
plt.plot(xx,y2,'--',label="n th partial sum",color='r')
plt.axvline(x=0)
plt.axhline(y=0)
plt.grid(True)
plt.title("Exp(x)")
plt.xlabel("x-axis$\\rightarrow$")
plt.ylabel("y-axis$\\rightarrow$")
plt.legend(loc="best",fontsize=15)
plt.show()
        
        
    
    
