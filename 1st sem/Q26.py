"""to find out largest and smallest element
of the matrix and corresponding index position"""

a=[[5,8,4],[3,4,1],[3,4,5]]
nr=len(a)
nc=len(a[0])
a1=a[0][0]
i1=1
j1=1
a2=a[0][0]
i2=1
j2=1
for i in range (nr):
    for j in range (nc):
        if(a1<=a[i][j]):
            a1=a[i][j]
            i1=i+1
            j1=j+1
        if(a2>=a[i][j]):
            a2=a[i][j]
            i2=i+1
            j2=j+1
print("largest",i1,j1,a1)
print("smallest",i2,j2,a2)

