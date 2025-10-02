import numpy as np

def f(x,t):
    h= 6.62607015 * 10**(-34)
    c= 299792458
    k= 1.38 * 10**(-23)
    pi= np.pi 
    e= np.exp
    y= 2*pi*h*c**2/(x**5*e(h*c/(x*k*t)))
    return y

yy=[]
A= 10**(-10)
xi=4000*A # wavelength range
xf=7000*A #wavelength range 
n=1000
s=0
t=3000 #temperature 
h=(xf-xi)/(n-1)
for i in range(0,n):
    x=xi+i*h
    y=f(x,t) 
    yy.append(y)     
for i in range(1,n-1):
    s=s+2*yy[i]
s=s+yy[0]+yy[n-1]   
m=s*h/2 
m=round(m,4)
print(m)
