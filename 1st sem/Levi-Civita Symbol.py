def levicivita (i,j,k):
    if (i==j or j==k or k==i):
        return 0
    elif ((i==0 and j==1 and k==2) or (i==1 and j==2 and k==0) or (i==2 and j==0 and k==1)):
         return 1
    else:
         return -1

a=[1,2,3]
b=[3,1,2] 
c=[]       
s=0
for i in range(3):
    for j in range(3):
        for k in range(3):
            p =levicivita(i,j,k)*a[j]*b[k]
            s=s+p
    c.append(s)
    s=0
print(c)
