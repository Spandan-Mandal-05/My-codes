#Forced Oscillator
import matplotlib.pyplot as plt
import numpy as np

#Define the equation of motion
def dgdt(v,x,t): 
    F=0.2
    s=2
    Rm=2
    m=4
    w=np.pi/8
    return (F/m*np.cos(w*t))-s/m*x-Rm/m*v

t=0
x=0.3
dxdt=v=-0.3
tf=30
n=10**4
h=(tf-t)/(n-1)
xx,vv,tt=[x],[dxdt],[t]
for i in range(n):
    v=v+h*dgdt(v,x,t)
    x=x+h*v
    t=t+h
    vv.append(v)
    xx.append(x)
    tt.append(t)

fig,ax=plt.subplots(2,1,figsize=(8,8),constrained_layout=True)
ax[0].plot(tt,xx,'--',color="red") 
ax[0].plot(tt,vv,'-.',color="green") 
ax[0].axvline(x=0,color='Black')
ax[0].axhline(y=0,color='Black')
ax[0].grid(True)
ax[0].set_ylabel("velocity or displacement $\\rightarrow$")
ax[0].set_xlabel("time $\\rightarrow$")
ax[0].set_title("Plot of v(t) vs time & x(t) vs time")
                
ax[1].plot(xx,vv,'-',color="green") 
ax[1].axvline(x=0,color='Black')
ax[1].axhline(y=0,color='Black')
ax[1].grid(True)
ax[1].set_ylabel("v(t)$\\rightarrow$")
ax[1].set_xlabel("x(t)$\\rightarrow$")
ax[1].set_title("Plot of v(t) vs x(t)")
plt.show()
