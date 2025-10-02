import matplotlib.pyplot as plt
a=-5
b=5
n=500
h=(b-a)/(n-1)
xx,yy=[],[]
for i in range (n):
    x=a+i*h
    xx.append(x)
    y=x*(x-1)
    yy.append(y)

mx=yy[0]
j=0
for i in range(n):
    if mx<yy[i]:
        mx=yy[i]
        j=i
print(xx[j],mx)
    
plt.plot(xx,yy,color='r')
plt.title("a simple plot")
plt.xlabel("x axis$\\rightarrow$")
plt.ylabel("y axis$\\rightarrow$")
plt.grid(True)
plt.axvline(x=0,color='b')
plt.axhline(y=0,color='b')
plt.show()
           
    
