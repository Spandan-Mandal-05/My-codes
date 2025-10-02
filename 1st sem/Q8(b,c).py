""" Write a Python program to arrange the array in descending order.
     Write a Python program to arrange the array in ascending order. 
"""

a=[0.1,2.1,-1.3,5.2,-1.0,5.0,4.3,3.7,7.1,4.6,-2.8,1.8]
xx=[]
yy=[]
n=len(a)
for i in range(0,n-1):
    for j in range(i+1,n):
        if(a[i]<a[j]):
            t=a[i]
            a[i]=a[j]
            a[j]=t
    xx.append(a[i])
xx.append(a[j])    
for i in range(0,n-1):
    for j in range(i+1,n):
        if(a[i]>a[j]):
            t=a[i]
            a[i]=a[j]
            a[j]=t
    yy.append(a[i])
yy.append(a[j])    
print(a)
print("descending order=",xx)
print("ascending order=",yy)
