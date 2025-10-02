import matplotlib.pyplot as plt 
import numpy as np
def f(x,v,t):
    if x==1:
        return (-g-r*v)
    elif x==-1:    
        return (g-r*v)
    elif x==2:
        return (-g-r*v**2)
    elif x==-2:
        return (g-r*v**2)
    
g=9.8
r=5
u1=10
u2=0
h=10**(-4)
t=0
tt1,tt2,tt3,tt4,vv1,vv2,vv3,vv4=[],[],[],[],[],[],[],[]

x=1
while (u1>=0):
    u1=u1+h*f(x,u1,t)
    tt1.append(t)
    t=t+h
    vv1.append(u1)

t=0
x=-1
while (f(x,u2,t)>=g/1000):
    u2=u2+h*f(x,u2,t)
    tt2.append(t)
    t=t+h
    vv2.append(u2)

u1=10
u2=0
t=0
x=2
while (u1>=0):
    u1=u1+h*f(x,u1,t)
    tt3.append(t)
    t=t+h
    vv3.append(u1)

t=0
x=-2
while (f(x,u2,t)>=g/1000):
    u2=u2+h*f(x,u2,t)
    tt4.append(t)
    t=t+h
    vv4.append(u2)


fig,ax=plt.subplots(2,2,figsize=(4,4),constrained_layout=True)

ax[0][0].plot(tt1,vv1,"blue",label= f"time required {max(tt1):.3f}")
ax[0,0].set_title("Throwing ball with $ R_m \\propto v$")
ax[0][0].legend()
ax[0][0].grid(True)
ax[0][0].axvline(x=0)
ax[0][0].axhline(y=0)
ax[0][0].set_xlabel("Time $\\rightarrow$" )
ax[0][0].set_ylabel("Velocity $\\rightarrow$")

ax[0][1].plot(tt2,vv2,"green",label=f"Required Time: {max(tt2):.3f},velocity: {max(vv2):.3f}")
ax[0,1].set_title("Releasing ball with $ R_m \\propto v$")
ax[0][1].legend()
ax[0][1].grid(True)
ax[0][1].axvline(x=0)
ax[0][1].axhline(y=0)
ax[0][1].set_xlabel("Time $\\rightarrow$" )
ax[0][1].set_ylabel("Velocity $\\rightarrow$")

ax[1][0].plot(tt3,vv3,"red",label= f"time required {max(tt3):.3f}")
ax[1,0].set_title("Throwing ball with $ R_m \\propto v^2$")
ax[1][0].legend()
ax[1][0].grid(True)
ax[1][0].axvline(x=0)
ax[1][0].axhline(y=0)
ax[1][0].set_xlabel("Time $\\rightarrow$" )
ax[1][0].set_ylabel("Velocity $\\rightarrow$")

ax[1][1].plot(tt4,vv4,"black",label=f"Required Time: {max(tt4):.3f},velocity: {max(vv4):.3f}")
ax[1,1].set_title("Releasing ball with $ R_m \\propto v^2$")
ax[1][1].legend()
ax[1][1].grid(True)
ax[1][1].axvline(x=0)
ax[1][1].axhline(y=0)
ax[1][1].set_xlabel("Time $\\rightarrow$" )
ax[1][1].set_ylabel("Velocity $\\rightarrow$")
plt.show()
    