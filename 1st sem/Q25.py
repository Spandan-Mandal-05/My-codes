import numpy as np
m=[[3,2,6,4],[1,4,2,5],[3,5,2,6]]
nr=len(m)
nc=len(m[0])
c=np.ones([nc,nr])
for i in range(nr):
    for j in range(nc):
        c[j][i]=m[i][j]
print(c)
