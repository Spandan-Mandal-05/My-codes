import numpy as np

def f(mode,x):
    if mode==1:
        return np.pi**(-1/4)*np.exp(-x**2/2)
    if mode==2:
        return (4*np.pi)**(-1/4)*(2*x**2-1)*np.exp(-x**2/2)

xx=np.linspace(-10**3,10**3,10**5+1)
h=abs(xx[1]-xx[0])
yy1=f(1,xx)
yy2=f(2,xx)
yy=yy1*yy2
n=len(xx)
g,m=0,0
for j in range (0,n//2):
    g=g+4*yy[2*j+1]
    if 2*j+2 < (n-1):
        m=m+2*yy[2*j+2]
s=h/3*(yy[0]+g+m+yy[n-1])
print(round(s,4))