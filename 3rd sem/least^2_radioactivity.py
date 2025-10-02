import matplotlib.pyplot as plt
import numpy as np
plt.style.use("classic")

time = x = np.arange(0,4.5,0.5)
activity = np.array([1.5,0.909,0.552,0.334,0.203,0.123,0.075,0.045,0.027])
ln_activity = y = np.log(activity)
n=len(x)

z=(np.sum(x**2)*n-np.sum(x)*np.sum(x))
c = (np.sum(x**2)*np.sum(y)-np.sum(x)*np.sum(x*y))/z
m=(np.sum(x*y)*n-np.sum(x)*np.sum(y))/z

xx=np.linspace(-0.2,4.2,100)
ln_activity_fit=(m*xx+c)

fig,ax=plt.subplots(2,1,figsize=(8,8),constrained_layout=True)

ax[0].plot(time,activity,'*')
ax[0].plot(xx,np.exp(m*xx+c))
ax[0].legend(loc="best")
ax[0].grid(True)

ax[1].plot(time,ln_activity,'*',label=f"Half Life = {-m*np.log(2)}")
ax[1].plot(xx,ln_activity_fit,'-b',label=f'Decay Rate = {-m}')
ax[1].legend(loc="best")
ax[1].grid(True)
plt.show()
