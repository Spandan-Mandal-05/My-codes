"""Speed (in some unit) of few particles are provided bellow in a list
[1.2, 2.4, 9.0, 1.8, 5.8, 3.0, 4.9, 8.7, 2.2, 3.1].
Write down a Python programming to find out the followings:
(a) Maximum speed and corresponding particle index.
(b) Minimum speed and corresponding particle index.
(c) Average speed.
(d) RMS speed.
(e) Standard deviation of speed distribution"""

v=[1.2, 2.4, 9.0, 1.8, 5.8, 3.0, 4.9, 8.7, 2.2, 3.1]
n=len(v)
m1=v[0]
j=0
m2=v[0]
k=0
for i in range(n):
    if(m1<v[i]):
        m1=v[i]
        j=i
    if(m2>v[i]):
        m2=v[i]
        k=i
print("max speed is",m1," and corresponding particle index",j+1 )
print("max speed is",m2," and corresponding particle index",k+1 )

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
