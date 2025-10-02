v1=[0.9 ,2.0, -0.8, 1.2, 1.2, -2.5, 1.9, -1.6, 2.8, 1.2]
v2=[0.9, -2.0 ,-0.8, 1.2, 1.2, 2.5, -1.9, 1.6, 2.8, -1.2]
v3=[-0.9, 2.0, 0.8, -1.2, -1.2, 2.5, 1.9, -1.6, 2.8, 1.2]
v=[]
n=len(v1)
for i in range(n):
    s=(v1[i]**2+v2[i]**2+v3[i]**2)**0.5
    v.append(s)
s=0
m=0
for i in range(n):
    s=s+v[i]
    m=m+v[i]**2
avg=s/n
rms=(m/n)**0.5
s=0
for i in range(n):
    s=s+(avg-v[i])**2
std=(s/n)**0.5
print("average speed =",avg)
print("rms sped =",rms)
print("standard deviation =",std)     
