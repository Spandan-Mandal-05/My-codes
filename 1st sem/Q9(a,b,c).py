""" Rectangular Cartesian components of two
vectors are given by, 𝐴⃗ = (1, 2, 1)  and ⃗𝐵 = (2, 4, 3)
 and |𝐵|⃗ """
import numpy as np
a=[1,2,1]
b=[2,4,3]
n=3
s1=0
s2=0
s3=0
for i in range(n):
    s1=s1+a[i]*a[i]
    s2=s2+b[i]*b[i]
    s3=s3+ a[i]*b[i]
aa=s1**0.5
bb=s2**0.5
ang=s3/(s1*s2)
ang=np.arccos(ang)
ang=ang*np.pi/180
print("(a) |𝐴|⃗=",aa," and |⃗𝐵|=",bb)
print("(b) Angle between 𝐴⃗ and 𝐵⃗= ",ang)

c=[]
c1=a[1]*b[2]-a[2]*b[1]
c2=a[2]*b[0]-a[0]*b[2]
c3=a[0]*b[1]-a[1]*b[0]
c.append(c1)
c.append(c2)
c.append(c3)
print("(c) The vector 𝐴 ×⃗ 𝐵⃗=",c)

s=0
for i in range(n):
    s=s+c[i]*c[i]
area=0.5*s**0.5

print("(d) Area of the triangle formed by two vectors",area)





    
    
