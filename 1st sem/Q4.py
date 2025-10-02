# Write a Python program to get all factors of a given number

a=345
aa=[]
for i in range(1,a+1):
    if(a%i==0):
        aa.append(i)
print(aa)
