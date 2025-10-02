m=[1.1,2.0,3.0,1.9,1.7,2.1,2.9,1.2,1.8,2.2]
v1=[0.9, 2.0 ,-0.8 ,1.2 ,1.2 ,-2.5 ,1.9 ,-1.6 ,2.8,1.2]
v2=[0.9, -2.0, -0.8 ,1.2, 1.2, 2.5 ,-1.9, 1.6 ,2.8, -1.2]
v3=[-0.9 ,2.0, 0.8, -1.2, -1.2, 2.5 ,1.9, -1.6, 2.8, 1.2]
p=[]
pp=[]
p1=[]
p2=[]
p3=[]
t=[]
s2=0
s4=0
s6=0
s10=0
n=len(m)
for i in range(n):
    s1=m[i]*v1[i]
    s2=s2+s1
    s3=m[i]*v2[i]
    s4=s4+s3
    s5=m[i]*v3[i]
    s6=s6+s5
    s7=(v1[i]**2+v2[i]**2+v3[i]**2)**0.5
    s8=m[i]*s7
    s9=1/2*m[i]*s7**2
    s10=s10+s9
    p1.append(s1)
    p2.append(s3)
    p3.append(s5)
    p.append(s8)
    t.append(s9)
pp.append(s2)
pp.append(s4)
pp.append(s6)
print("list corresponding to px=",p1)
print("list corresponding to py=",p2)
print("list corresponding to pz=",p3)
print("a list of | p⃗| =",p)
print("list of kinetic energies (𝑇) =",t)
print("Total K.E. =",s10)
print("Total linear momentum ⃗p=",pp)
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








    
    
