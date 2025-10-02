import numpy as np
import matplotlib.pyplot as plt
"""
def f(t):
    return (1+a*t+b*t**2)

a= 5.21*10**(-3)
b=7.20*10**(-7)
temperature=np.arange(127,2727,200)
td=527
Rt_Rd=f(temperature)/f(td)
temp_K=temperature+273
plt.scatter(temp_K,Rt_Rd)
plt.grid(True)
plt.show()"""
Temp=np.array([843,968,1061,1145,1220,1289,1353,1409,1465,1517,1566,1610,1655,1697,1739,1778,1814,1848,1885])
R=np.array([3.289,3.742,4.087,4.408,4.694,4.966,5.219,5.445,5.671,5.887,6.086,6.270,6.462,6.640,6.818,6.985,7.142,7.291,7.452])
Rd=2.1984025
Temp_K=Temp+273
Rt_Rd=R/Rd
