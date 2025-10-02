import numpy as np
a=np.array([[3,4,1,2],[-3,2,1,5],[-2,-6,4,-3],[2,-5,-3,-1]])
nr=len(a)
nc=len(a[0])
ta=np.ones([nc,nr])
for i in range(nr):
    for j in range(nc):
        ta[j][i]=a[i][j]
print(ta)
if np.array_equal(a,ta):
    print("Symmetric Matrix ")
elif np.array_equal(a,-ta):
    print("Anti-symmetric Matrix")
else:
    print("Neither Symmetric nor Anti-symmetric Matrix")

nr=len(a)
nc=len(a[0])
b=np.ones([nr,nc])
for i in range(nr):
    for j in range(nc):
        s=0
        for k in range(nc):
            s=s+a[i][k]*ta[k][j]
        b[i][j]=s    
print(b)
if b==[[1,0,0,0],[0,1,0,0],[0,0,1,0],[0,0,0,1]]:
    print("Orthogonal Matrix")
else:
    print("non-Orthogonal Matrix") 

