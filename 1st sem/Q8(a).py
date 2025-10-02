"""Write a Python program to get the max. and min. element from the array """
a=[0.1,2.1,-1.3,5.2,-1.0,5.0,4.3,3.7,7.1,4.6,-2.8,1.8]
n=len(a)
m1=a[0]
j=0
m2=a[0]
k=0
for i in range(n):
    if(m1<a[i]):
        m1=a[i]
        j=i
    if(m2>a[i]):
        m2=a[i]
        k=i
print("position",j,"max number is",m1)
print("position",k,"min number is",m2)
