import matplotlib.pyplot as plt
import numpy as np
plt.style.use("classic")
Load=x=np.arange(0,0.12,0.02)
Depresssion=y=np.array([0,	0.0013,	-0.0037	,-0.0003	,0.0787,	0.0805])
g=9.8
miu = 0.00127
n=len(x)

z=(np.sum(x**2)*n-np.sum(x)*np.sum(x))
c = (np.sum(x**2)*np.sum(y)-np.sum(x)*np.sum(x*y))/z
m=(np.sum(x*y)*n-np.sum(x)*np.sum(y))/z

std = np.sqrt(np.sum(((m*x+c)-y)**2)/(n-2))

xx=np.linspace(-0.02,0.12,100)
y_error = 0.01
plt.errorbar(Load, Depresssion,
            yerr = std,
            fmt ='o',
            label=("$frequency_{longitudinal}$=" f"{(g/(miu*m))*0.5}", f"slope ={m}"))
#plt.plot(Load,Depresssion,'*')
plt.plot(xx,m*xx+c,'-')
plt.grid(True)
plt.legend(loc="best")
plt.show()
