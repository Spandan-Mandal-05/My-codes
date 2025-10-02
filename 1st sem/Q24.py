import matplotlib.pyplot as plt
a=-2
b=2
n=500
h=(b-a)/(n-1)
xx,yy=[],[]
for i in range (n):
    x=a+i*h
    xx.append(x)
    y=x**4 - x**2
    yy.append(y)
    
#To find out the maxima and minima of 𝑦(𝑥) and corresponding values of 𝑥
m1=yy[0]
j=0
m2=yy[0]
k=0
for i in range(n):
    if m1<yy[i]:
        m1=yy[i]
        j=i
    if m2>yy[i]:
        m2=yy[i]
        k=i
print("minimum =",xx[k],m2)    
print("maximum=",xx[j],m1)

# To plot a simple function 
plt.plot(xx,yy,color='r')
plt.title("a simple plot")
plt.xlabel("x-axis$\\rightarrow$")
plt.ylabel("y-axis$\\rightarrow$")
plt.legend("y(x)")
plt.grid(True)
plt.axvline(x=0)
plt.axhline(y=0)
plt.ylim(-1,5)
plt.show()
           
