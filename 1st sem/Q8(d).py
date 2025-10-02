"""Write a Python program to calculate average of 𝑎,
RMS of 𝑎 and standard deviation of 𝑎 """
a=[0.1,2.1,-1.3,5.2,-1.0,5.0,4.3,3.7,7.1,4.6,-2.8,1.8]
n=len(a)
s=0
m=0
for i in range(n):
    s=s+a[i]
    m=m+a[i]**2
avg=s/n
rms=(m/n)**0.5
s=0
for i in range(n):
    s=s+(avg-a[i])**2
std=(s/n)**0.5
print("average=",avg)
print("rms=",rms)
print("standard deviation=",std)
