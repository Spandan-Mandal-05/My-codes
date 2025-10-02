#Checking Orthogonality of Trigonometric Functions 
import numpy as np  
import matplotlib.pyplot as plt
#plt.style.use("classic")

#Define simpson integral
def integral(mode,i,j):
    xx=np.linspace(-np.pi,np.pi,10**2+1)
    if mode==0:
        yy=np.cos(i*xx)*np.cos(j*xx)
    elif mode==1:
        yy=np.sin(i*xx)*np.sin(j*xx)
    h=abs(xx[1]-xx[0])
    n=len(xx)
    g,m=0,0
    for k in range (0,n//2):
        g=g+4*yy[2*k+1]
        if 2*k+2 < (n-1):
            m=m+2*yy[2*k+2]
    s=h/3*(yy[0]+g+m+yy[n-1])
    return (s/np.pi)

n=10
for i in range (1,n):
    for j in range (1,n):
        integral_cos = round(integral(0, i, j), 2)
        integral_sin = round(integral(1, i, j), 2)
        
        if integral_cos == 1 or integral_sin == 1:
            plt.scatter(i, j, marker='+',color='red', label='1')
        if integral_cos == 0 or integral_sin == 0:
            plt.scatter(i, j, marker='o',color='green',label='0')
            
handles, labels = plt.gca().get_legend_handles_labels()
by_label = dict(zip(labels, handles))
plt.legend(by_label.values(), by_label.keys())

plt.xlabel('i$\\rightarrow$')
plt.ylabel('j$\\rightarrow$')
plt.grid(True)
plt.title('Checking Orthogonality of Trigonometric Terms')
plt.show()

