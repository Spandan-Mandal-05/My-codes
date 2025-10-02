#matrix addition & substraction
a=[[1,2,0],[2,1,0],[3,0,1]]
b=[[-1,0,2],[-3,2,1],[0,3,-2]]
nr=len(a)
nc=len(a[0])
ss1,ss2=[],[]
for i in range(nr):
    s1,s2=[],[]
    for j in range (nc):
        g1= a[i][j]+b[i][j]
        g2=a[i][j]-b[i][j]
        s1.append(g1)
        s2.append(g2)
    ss1.append(s1)
    ss2.append(s2)
print("addition =",ss1,"substraction =",ss2)

#matrix multiplication
ss1,ss2=[],[]
for i in range(nr):
    s1,s2=[],[]
    for j in range (nc):
        g1,g2=0,0
        for k in range (nr):
            g1=g1+a[i][k]*b[k][j]
            g2=g2+b[i][k]*a[k][j]
        s1.append(g1)
        s2.append(g2)
    ss1.append(s1)
    ss2.append(s2)
ab=ss1
ba=ss2
print("AB =",ab,"BA =",ba)

nr=len(ab)
nc=len(ab[0])
ss=[]
for i in range(nr):
    s=[]
    for j in range (nc):
        g=ab[i][j]-ba[i][j]
        
        s.append(g)
    ss.append(s)
print("AB-BA =",ss)


       
