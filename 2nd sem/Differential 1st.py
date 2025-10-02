import numpy as np
import matplotlib.pyplot as plt 

#x=np.arange(-10,10,0.1)
x1=-0
x2=10
n=200
h=(x2-x1)/(n-1) 
y=0
i = 0
xx,yy,x3,y3=[],[],[],[]
while i<=n:
    xx.append(x1)
    yy.append(y)
    if i%5==0:
        x3.append(x1)
        y3.append(y)
    y=y + h*(-x1*y**2+1)   #Put the slope equation 
    x1 += h
    i+=1
    
print(x3,y3)
plt.plot(xx,yy,color='blue')
plt.scatter(x3,y3)
plt.axvline(x=0,color='red') 
plt.axhline(y=0,color='red')
# plt.xlim(-2,2)
plt.grid()
# plt.ylim(-5,150)
plt.show()   
