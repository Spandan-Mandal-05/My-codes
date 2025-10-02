import numpy as np
import matplotlib.pyplot as plt

def f(vc):
    return (vi-vc)/(R*C)
vi=10
R= 1000
C= 100e-6
t=0
vc=0
tf=0.5
n=10000
h=(tf-t)/(n-1)
Vc,T=[],[]
while vc<=vi*0.999:
    Vc.append(vc)
    T.append(t)
    t=t+h
    vc=vc+f(vc)*h

plt.plot(T,Vc,label=f"time required= {t:.5f}")
plt.axvline(x=0,color='Black',alpha=0.5,)
plt.axhline(y=0,color='Black',alpha=0.5)
plt.grid(True)
plt.title("Transient Phenomena of RC Circuit")
plt.ylabel("Vc $\\rightarrow$")
plt.xlabel("Time $\\rightarrow$")
plt.legend(loc="best")
plt.show()