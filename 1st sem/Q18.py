import numpy as np
m=40
x=30*np.pi/180
ss=[]

for n in range(1,m+1):
    s=0
    fact=1
    k=0
    for i in range (1,2*n+1):
        fact=fact*i
        if(i%2==1):
            g=(x**i)/fact
            s=s+g*(-1)**k
            k=k+1
    ss.append(s)
    
t=10**(-6)
for n in range(0,m-1):
    if(abs(ss[n+1]-ss[n])<=t):
        print(n,ss[n])
        break
