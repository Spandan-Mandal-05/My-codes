import matplotlib.pyplot as plt
import numpy as np
a=-0.5
b=1
n=100
h=(b-a)/(n-1)
xx,y1,y2,y3=[],[],[],[]
for i in range (n):
    x=a+i*h
    xx.append(x)
    s1=-1/24*np.exp(-5*x)+25/24*np.exp(-x/5)
    s2=(1+x)*np.exp(-x)
    s3=np.exp(-5/13*x)*(5/12*np.sin(12/13*x)+np.cos(12/13*x))
    y1.append(s1)
    y2.append(s2)
    y3.append(s3)

plt.plot(xx,y1,'--',color="r",label="Over-damped")
plt.plot(xx,y2,'.',color="g",label="Critically-damped")
plt.plot(xx,y3,'-',color="b",label="oscilatory")
plt.axvline(x=0)
plt.axhline(y=0)
plt.ylim(0.6,1.05)
plt.legend(loc="best",fontsize=15)        
plt.title("oscilatory motion")
plt.grid(True)
                        
plt.show()
