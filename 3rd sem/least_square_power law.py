import matplotlib.pyplot as plt
import numpy as np
plt.style.use("classic")

xx=np.array([2,4,7,10,20,40,60])
yy=np.array([43,25,18,13,8,5,3])
lnx= x = np.log(xx)
lny= y = np.log(yy)
n=len(x)

z=(np.sum(x**2)*n-np.sum(x)*np.sum(x))
c = (np.sum(x**2)*np.sum(y)-np.sum(x)*np.sum(x*y))/z
m=(np.sum(x*y)*n-np.sum(x)*np.sum(y))/z

xx2=np.linspace(1,62,100)

fig,ax=plt.subplots(2,1,figsize=(8,8),constrained_layout=True)

ax[0].plot(xx,yy,'*')
ax[0].plot(xx2,np.exp(m*np.log(xx2)+c),'-')
ax[0].legend(loc="best")
ax[0].grid(True)

ax[1].plot(lnx,lny,'*')
ax[1].plot(np.log(xx2),m*np.log(xx2)+c,'-r',label=f"b={m} & a={np.exp(c)}")
ax[1].legend(loc="best")
ax[1].grid(True)

plt.show()
