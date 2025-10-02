#Comaparison of Euler and Modified Euler
import matplotlib.pyplot as plt
import numpy as np
plt.style.use("classic")

def d2y_dx2(x,y,g):
	e=np.exp
	return (-e(x)*g)-y+(2*(x-1)*e(-x))-x+1
	
def y1(x):
	return x*np.exp(-x)
n=100 #no of points	
xi=x=0
xf=4
y=0
g=1
h=(xf-xi)/(n-1)

xx,yy=[xi],[y1(x)]
yy_euler=[y]

#Euler Method
for i in range(n):

	g=g+h*d2y_dx2(x,y,g)
	y=y+h*g
	x += h
	yy.append(y1(x))
	xx.append(x)
	yy_euler.append(y)
	
xi=x=0
xf=4
y=0
g=1	
h=(xf-xi)/(n-1)

#Modified Euler
yy_modified=[y]
for i in range(n):
	xn=x
	yn=y
	gn=g
	g=gn+h*d2y_dx2(x,y,g)
	y=yn+h*g
	x +=h
	g=gn+0.5*h*(d2y_dx2(xn,yn,gn) + d2y_dx2(x,y,g))	
	y=yn+0.5*h*(gn+g)	
	yy_modified.append(y)

plt.plot(xx,yy,'-',label="Real Plot")
plt.plot(xx,yy_euler,'o',label="Euler")
plt.plot(xx,yy_modified,'*',label="Modified Euler")
plt.ylabel("f(x) $\\rightarrow$")
plt.xlabel("x $\\rightarrow$")
plt.grid(True)
plt.legend(loc="best")
plt.show()	
