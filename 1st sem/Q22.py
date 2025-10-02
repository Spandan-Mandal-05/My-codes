#Plot the following functions 𝑒^𝑥 and 𝑒^−𝑥 within x‑range [–2,2] and y‑range [0,2]

import matplotlib.pyplot as plt
import numpy as np
a=-2
b=2
n=100
h=(b-a)/(n-1)
xx,y1,y2=[],[],[]
for i in range (n):
    x=a+i*h
    xx.append(x)
    s1=np.exp(x)
    s2=np.exp(-x)
    y1.append(s1)
    y2.append(s2)

plt.plot(xx,y1,'-',label="e^x",color='g')
plt.plot(xx,y2,'--',label="e^(-x)",color='b')
plt.xlabel("x-axis$\\rightarrow$")
plt.ylabel("y-axis$\\rightarrow$")
plt.grid(True)
plt.axvline(x=0)
plt.axhline(y=0)
plt.ylim(0,2)
plt.legend(loc="best",fontsize=15)
plt.show()
    
