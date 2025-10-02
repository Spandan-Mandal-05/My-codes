import matplotlib.pyplot as plt
import numpy as np

def f(t,k1,k2,x1,x2,x3): # define the Radioactive Disintegration
    e=np.exp
    y1=(-k1*x1)
    y2=(-k2*x2)+(k1*x1)
    y3=(k2*x2)
    return y1,y2,y3

k1=1
k2=3
ti=0
tf=6
x1=1
x2=0
x3=0
s=x1+x2+x3
n=10000
h=(tf-ti)/(n-1)
tt,yy1,yy2,yy3,ss=[],[],[],[],[]
for i in range (n):
    t=ti+i*h
    y1,y2,y3=f(t,k1,k2,x1,x2,x3)
    x1=x1+h*y1
    x2=x2+h*y2
    x3=x3+h*y3
    s=x1+x2+x3
    yy1.append(x1)
    yy2.append(x2)
    yy3.append(x3)
    tt.append(t)
    ss.append(s)

plt.plot(tt,yy1,'-.',label="$N_A(t)$",color="red") 
plt.plot(tt,yy2,'--',label="$N_B(t)$",color="green") 
plt.plot(tt,yy3,':',label="$N_C(t)$",color="blue")
plt.plot(tt,ss,'-',label="N",color="brown")
plt.axvline(x=0,color='Black')
plt.axhline(y=0,color='Black')
plt.grid(True)
plt.title("Radioactive Disintegration")
plt.ylabel("N(t) $\\rightarrow$")
plt.xlabel("Time(t) $\\rightarrow$")
plt.legend(loc='best',fontsize=15)
plt.show()