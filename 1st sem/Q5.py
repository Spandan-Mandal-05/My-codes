""" Write a Python program which will give you sum of all
digits of a 𝑛−digit (𝑛 ≥ 2) number say a """

a=237649
s=0
n=len(str(a))
for i in range(n-1,0-1,-1):
    b=a%10**i
    c=(a-b)/10**i
    a=b
    s=s+c
print(s)

a=237649
s=0
n=len(str(a))
for i in range (1,n
