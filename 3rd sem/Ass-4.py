#integration and it's Least Square Fitting
import numpy as np  
import matplotlib.pyplot as plt
#plt.style.use("classic")

#defining the integral
def integral(lamda):
    xx=np.linspace(0.001,100,10**3+1)
    yy=xx**3/(np.exp(xx/lamda)-1)
    h=abs(xx[1]-xx[0])
    n=len(xx)
    integral_value=yy[0]+yy[n-1]
    integral_value += 4*np.sum(yy[1:n-1:2])
    integral_value += 2*np.sum(yy[2:n-2:2])
    integral_value *= h/3
    return (integral_value)

lamdas = np.arange(1, 2.1, 0.1)
integrals = [integral(lamda) for lamda in lamdas] 
ln_lamdas = x = np.log(lamdas)
ln_integrals = y = np.log(integrals)
n = len(x)

#Least Square Fitting
z=(np.sum(x**2)*n-np.sum(x)*np.sum(x))
c = (np.sum(x**2)*np.sum(y)-np.sum(x)*np.sum(x*y))/z
m=(np.sum(x*y)*n-np.sum(x)*np.sum(y))/z

xx2=np.linspace(0.8,2.2,30)
fig,ax=plt.subplots(2,1,figsize=(8,8),constrained_layout=True)

ax[0].plot(lamdas, integrals,'*',color='black',label="Real Points")
ax[0].plot(xx2,np.exp(m*np.log(xx2)+c),'-',color='black',label="Square Fitted")
ax[0].set_xlabel('λ$\\rightarrow$')
ax[0].set_ylabel('Integral$\\rightarrow$')
ax[0].set_title('Plot of Integrals vs λ')
ax[0].legend(loc="best")
ax[0].grid(True)

ax[1].plot(ln_lamdas,ln_integrals,'^',color='black',label="Real Points")
ax[1].plot(np.log(xx2),m*np.log(xx2)+c,'-r',color='black',label="Square Fitted")
ax[1].text(-0.2,4,f"slope={m:.3f} & intersept={c:.3f}")
ax[1].set_xlabel('ln(λ)$\\rightarrow$')
ax[1].set_ylabel('ln(Integral)$\\rightarrow$')
ax[1].set_title('Plot of ln(Integrals) vs ln(λ)')
ax[1].legend(loc="best")
ax[1].grid(True)

plt.show()