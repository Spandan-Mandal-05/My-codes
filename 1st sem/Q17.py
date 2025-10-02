m=40
x=0.5
ss=[]
for n in range(1,m):
    fact=1
    s=1
    for i in range(1,n+1):
        fact=fact*i
        s=s+x**i/fact
    ss.append(s)
t=10**(-5)

for n in range(0,m):
	r=abs(ss[n]-ss[n-1])
	if(r<=t):
	    print(n+1,ss[n],r)
	    break
