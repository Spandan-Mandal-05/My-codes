import matplotlib.pyplot as plt
import numpy as np
a=-2*np.pi #use 3, 4, 5 pi to increase the range of graph 
b=2*np.pi #use 3, 4, 5 pi to increase the range of graph
n=1 #Please change the values of n to increase the number of Taylor terms 
m=60
h=(b-a)/(m-1)
xx,y1,y2=[],[],[]
for i in range (m):
    x=a+i*h
    xx.append(x)
    g=np.sin(x)
    y1.append(g)
    s=0
    fact=1
    k=0
    for j in range(1,2*n+1):
        fact=fact*j
        if(j%2==1):
            r=x**j/fact
            s=s+r*(-1)**k
            k=k+1
    y2.append(s)

plt.plot(xx,y1,'-',label="sin(x)",color='b')
plt.plot(xx,y2,'--',label=f"{n} th partial sum",color='r')
plt.grid(True)
plt.title("sin(x)")
plt.ylabel("y(x)$\\rightarrow$")
plt.xlabel("x$\\rightarrow$")
plt.legend(loc='best',fontsize=10)
plt.ylim(-1.5,1.5)
plt.show()
