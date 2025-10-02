import matplotlib.pyplot as plt
import numpy as np

def Y(l,s):
    return(p*(l**3)/s)

#taking initial values
m=10**(-2)
g=9.80665
b=1.3*m
d=0.792857143*m
p=g/(4*b*d**3)
l1=80*m
l2=90*m
l3=100*m
l80=[12.6999,12.6345,12.5383,12.4487,12.3463,12.2480]
l90=[12.5760,12.4655,12.3725,12.2616,12.1616,12.0747]
l100=[12.7060,12.5038,12.3000,12.1104,11.9172,11.7193]
mm=[0,.500,1.000,1.500,2.000,2.500]
mm.sort()
l80.sort(reverse=True)
l90.sort(reverse=True)
l100.sort(reverse=True)
dm,dl80,dl90,dl100,sp80,sp90,sp100,xx,yy80,yy90,yy100=[],[],[],[],[],[],[],[],[],[],[]
l=len(mm)

#calculating slope for 80,90,100 cm
for i in range(l):
    for j in range(i+1,l):
        dm.append(abs(mm[j]-mm[i]))
        dl80.append(abs(l80[j]-l80[i]))
        dl90.append(abs(l90[j]-l90[i]))
        dl100.append(abs(l100[j]-l100[i]))
        sp80.append((dl80[j-1]/dm[j-1]))
        sp90.append((dl90[j-1]/dm[j-1]))
        sp100.append((dl100[j-1]/dm[j-1]))
s80=np.average(sp80)*m
s90=np.average(sp90)*m
s100=np.average(sp100)*m
#calculating average experimental value for young's modulus
yy=[Y(l1,s80),Y(l2,s90),Y(l3,s100)]
YM=np.average(yy)
#plotting graph
xi=mm[0]
xf=mm[l-1]
n=200
d=(xf-xi)/(n-1)
sc=10**(14)
for i in range(n):
    x=xi+i*d
    x=sc*x
    y80=s80*x
    y90=s90*x
    y100=s100*x
    xx.append(x)
    #arrays for depression
    yy80.append(y80)
    yy90.append(y90)
    yy100.append(y100)
f=10**(-11)
print('Youngs modulus=',YM*f,'x 10^11')

plt.xlabel('Load M in kg $\\rightarrow$')
plt.ylabel('Depression l in m $\\rightarrow$')
plt.title('Estimated Youngs modulus')
plt.grid(True,'both')
plt.plot(xx,yy80,label='Average graph 80 cm')
plt.plot(xx,yy90,label='Average graph 90 cm')
plt.plot(xx,yy100,label='Average graph 100 cm')
plt.axhline(y=0)
plt.axvline(x=0)
plt.legend()
plt.show()