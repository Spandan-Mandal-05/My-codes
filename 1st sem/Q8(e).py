""" Write a Python program to create an array say 𝑏
such that 𝑏𝑖 = 𝑎2𝑖 . Hence, plot 𝑏 with respect to 𝑎 """

import matplotlib.pyplot as plt
a=[0.1,2.1,-1.3,5.2,-1.0,5.0,4.3,3.7,7.1,4.6,-2.8,1.8]
b=[]
n=len(a)
for i in range(n):
    c=a[i]**2
    b.append(c)
plt.plot(a,b)
plt.show()
    
    
