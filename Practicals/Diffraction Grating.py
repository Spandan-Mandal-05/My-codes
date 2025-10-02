import matplotlib.pyplot as plt
import pandas as pd
import numpy as np

df = pd.read_excel("C:/Spandan E/Diffraction Gratting.xlsx")
#print(df.columns)

Sin_Theta = y = df['Sin(Theta)'].iloc[0:15].to_numpy()
mn = x = df['Order of the slit'].iloc[0:15].to_numpy()
d = 1e-5
n = len(x)
#Least Square Fitting
z = (np.sum(x**2)*n-np.sum(x)*np.sum(x))
c = (np.sum(x**2)*np.sum(y)-np.sum(x)*np.sum(x*y))/z
m = (np.sum(x*y)*n-np.sum(x)*np.sum(y))/z


xx=np.linspace(-8,8,100)
plt.plot(mn,Sin_Theta,'*')
plt.plot(xx,m*xx+c,'-',label = f"Wavelength {m*d} m ,{m},{np.arctan(m):.4f} & {c:.4f}")
plt.grid(True)
plt.legend(loc="best")
#plt.show()
print(round(m*8+c,4))
