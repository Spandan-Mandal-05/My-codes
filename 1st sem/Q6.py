""" For a given number 𝑎, write a Python program
to check whether it is prime number """

a=7
aa=[]
for i in range(1,a+1):
    if(a%i==0):
        aa.append(i)
if(aa==[1,a]):
    print(a,"is a prime number")
else:
    print(a,"is not a prime number")
