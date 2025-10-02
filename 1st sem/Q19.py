"""to evaluate the partial sum of the series upto some given number
of terms (𝑁) for a given value of 𝑥"""

import numpy as np
m=30
x=60*np.pi/180
ss=[]

for n in range(1,m):
    s=1
    fact=1
    k=1
    for i in range(2,2*n+1):
        fact=fact*i
        if(i%2==0):
            g=(x**i)/fact
            s=s+g*(-1)**k
            k=k+1
    ss.append(s)

t=10**(-4)
for n in range (1,m-1):
    s=abs(ss[n]-ss[n-1])
    if (s<=t):
        print(ss[n])
        break
