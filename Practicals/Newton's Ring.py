import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_excel("C:/Spandan E/Book1.xlsx")
D2 = y = df['D2'].to_numpy()*10**(-4)
#R=2.2
lamda = 589*10**(-9)
mn = x = df['m'].to_numpy()
n = len(x)
#Least Square Fitting
z = (np.sum(x**2)*n-np.sum(x)*np.sum(x))
c = (np.sum(x**2)*np.sum(y)-np.sum(x)*np.sum(x*y))/z
m = (np.sum(x*y)*n-np.sum(x)*np.sum(y))/z

xx=np.linspace(-2,20,200)
plt.plot(mn,D2,'*',label=f"Radius {m/(4*lamda):.5f} m")
plt.plot(xx,m*xx+c,'-',label = f"Wavelength {lamda*10**(9)} nm ")
plt.grid(True)
plt.legend(loc="best")
plt.show()
#print(mn,D2)

