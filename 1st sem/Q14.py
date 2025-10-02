m=[1.1, 2.0, 3.0, 1.9, 1.7, 2.1, 2.9, 1.2, 1.8, 2.2]
v=[0.9, 2.0, 0.8, 1.2, 1.2, 2.5, 1.9, 1.6, 2.8, 1.2]
p=[]
t=[]
s3=0
n=len(m)
for i in range(n):
    s1=m[i]*v[i]
    s2=1/2*m[i]*v[i]**2
    s3=s3+s2
    p.append(s1)
    t.append(s2)
print("list of | ⃗𝑝| =",p)
print("list of kinetic energies (𝑇) of all particles =", t)
print ("total enery =" , s3)
n=len(p)
m1=p[0]
j=0
m2=p[0]
k=0
for i in range(n):
    if(m1<p[i]):
        m1=p[i]
        j=i
    if(m2>p[i]):
        m2=p[i]
        k=i
print("highest momentum =",m1," and corresponding particle index =",j+1 )
print("lowest momentum =",m2," and corresponding particle index =",k+1)        
n=len(t)
m1=t[0]
j=0
m2=t[0]
k=0
for i in range(n):
    if(m1<t[i]):
        m1=t[i]
        j=i
    if(m2>t[i]):
        m2=t[i]
        k=i
print("largest K.E. =",m1," and corresponding particle index =",j+1 )
print("smallest K.E. =",m2," and corresponding particle index =",k+1)         
       
 
    
