# Center of Mass Calculation
m=[1.1,2.0,3.0,1.9,1.7,2.1,2.9,1.2,1.8,2.2]
x=[0.9,2.0,-0.8,1.2,1.2,-2.5,1.9,-1.6,2.8,1.2]
y=[0.9,-2.0,-0.8,1.2,1.2,2.5,-1.9,1.6,2.8,-1.2]
z=[-0.9,2.0,0.8,-1.2,-1.2,2.5,1.9,-1.6,2.8,1.2]
s1,s2,s3,s4=0,0,0,0
n=len(m)
for i in range (n):
    s1=s1+m[i]
    s2=s2+m[i]*x[i]
    s3=s3+m[i]*y[i]
    s4=s4+m[i]*z[i]
xc=round(s2/s1,2)
yc=round(s3/s1,2)
zc=round(s4/s1,2)
print("position of com =",xc,"i^ +",yc,"j^ +",zc,"k^" )
