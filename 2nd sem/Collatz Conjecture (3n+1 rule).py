import matplotlib.pyplot as plt
import numpy as np 
plt.style.use("classic")


xf=1000000 # maximum seed value
xx2,yy2=[],[]
for j in range(5,xf+1):
    xx2.append(j)
    m=j
    n=0
    while(m!=1):
        n+=1
        if m%2==0:
          m=m/2
        else:
          m=3*m+1
    yy2.append(n)
point=np.argmax(yy2)-1

y=point
xx1,yy1=[],[]
i=0
while(y!=1):
    i+=1
    if y%2==0:
        y=y/2
        yy1.append(y)
    else:
        y=3*y+1
        yy1.append(y)
    xx1.append(i)
yy4=[np.log(x) for x in yy1]


xx3,yy3=[],[]
for k in range(max(yy2)):
   s=yy2.count(k)
   yy3.append(s)
   xx3.append(k)

fig,ax=plt.subplots(2,2,figsize=(10,10),constrained_layout=True)
ax[0,0].plot(xx1,yy1,"Black")
ax[0,0].set_title(f"Collatz Sequence of {point}")
ax[0,0].text(point,max(yy1),f"{max(yy1)}")
ax[0,0].grid(True)
ax[0,0].axvline(x=0,alpha=0.5)
ax[0,0].axhline(y=0,alpha=0.5)
ax[0,0].set_xlabel("steps no. $\\rightarrow$" )
ax[0,0].set_ylabel("step value $\\rightarrow$")

ax[0,1].plot(xx2,yy2,'--',color="red")
ax[1,0].plot(xx3,yy3,'--',color="blue")

slope,intercept=np.polyfit(xx1,yy4,1)
xx_fit=np.linspace(min(xx1),max(xx1),100)
yy_fit=slope*xx_fit+intercept

ax[1,1].plot(xx1,yy4,"black")
ax[1,1].plot(xx_fit,yy_fit)
ax[1,1].set_title(f"log distribution curve of {point}")
ax[1,1].axvline(x=0,alpha=0.5)
ax[1,1].axhline(y=0,alpha=0.5)
ax[1,1].set_xlabel("steps no. $\\rightarrow$" )
ax[1,1].set_ylabel("ln(step value) $\\rightarrow$")

ax[0,1].hist(xx2,weights=yy2,bins=range(2,xf+2),color="red")
ax[0,1].text(point+5,max(yy2)-15,f"maximum steps= {max(yy2)} at {point} ")
ax[0,1].set_title("Collatz_length of series of numbers")
ax[0,1].set_xlabel("seed no. $\\rightarrow$" )
ax[0,1].set_ylabel("Collatz Length $\\rightarrow$")

maxf=max(yy3)
most_step=np.argmax(yy3)

ax[1,0].hist(xx3,weights=yy3,bins=range(1,max(xx3)+1),color="blue")
ax[1,0].set_title(f"Frequency distribution upto {xf}")
ax[1,0].text(most_step+10,maxf-80,f"most probable steps= {most_step} of frequency= {maxf}")
ax[1,0].set_xlabel("no. of steps $\\rightarrow$" )
ax[1,0].set_ylabel("Frequency $\\rightarrow$")
plt.show()