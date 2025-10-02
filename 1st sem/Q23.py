"""Plot the following functions in a single graph
sin(𝑥) and cos(𝑥) within x‑range [0,7] and y‑range [–1.2,1.2]"""

import matplotlib.pyplot as plt
import numpy as np
a=0
b=7
n=100
h=(b-a)/(n-1)
xx,y1,y2=[],[],[]
for i in range(n):
    x=a+i*h
    xx.append(x)
    s1=np.sin(x)
    s2=np.cos(x)
    y1.append(s1)
    y2.append(s2)

plt.plot(xx,y1,'-',color='g',label="sin(x)")
plt.plot(xx,y2,'--',color='b',label="cos(x)")
plt.title("simple plot")
plt.xlabel("x-axis$\\rightarrow$")
plt.ylabel("y-axis$\\rightarrow$")
plt.grid(True)
plt.axvline(x=0)
plt.axhline(y=0)
plt.legend(loc="best",fontsize=10)
plt.ylim(-1.2,1.2)
plt.xlim(0,7)
plt.show()
    
