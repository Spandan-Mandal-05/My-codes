"""Write a Python program to list all the prime
numbers within given two numbers a and b"""

a=22
b=222
xx=[]
for i in range(a+1,b):
    yy=[]
    for j in range(1,i+1):
        if(i%j==0):
            yy.append(j)
    if(yy==[1,j]):
        xx.append(i)
n=len(xx)        
print(n,xx)            
