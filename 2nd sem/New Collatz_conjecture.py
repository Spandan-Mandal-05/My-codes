import matplotlib.pyplot as plt
import numpy as np 
plt.style.use("classic")

def collatz_sequence(n):
   yy=[n]
   while n!=1:
      n=n//2 if n%2==0 else 3*n+1 
      yy.append(n)
   return yy

def collatz_length(n):
   return len(collatz_sequence(n))
n=27
m=1000
# Collatz_sequence of n
steps=np.arange(0,collatz_length(n),1)
maxv=max(collatz_sequence(n))
# Collatz_length of series of numbers
seeds=np.arange(5,m+1,1)
collatz_lengths=[collatz_length(seed) for seed in seeds]
point=np.argmax(collatz_lengths)-1
# Collatz_Length frequency 
step,frequency=[],[]
for k in range(max(collatz_lengths)):
   s=collatz_lengths.count(k)
   frequency.append(s)
   step.append(k)
maxf=max(frequency)
most_step=np.argmax(frequency)

fig,ax=plt.subplots(2,2,figsize=(8,8),constrained_layout=True)
ax[0,0].plot(steps,collatz_sequence(n))
ax[0,0].set_title(f"Collatz Sequence of {n}")
ax[0,0].text(seeds[np.argmax(collatz_sequence(n))],maxv+0.04,f'Max={maxv}, total steps={max(steps)}')
ax[0,0].grid(True)
ax[0,0].axvline(x=0,alpha=0.5)
ax[0,0].axhline(y=0,alpha=0.5)
ax[0,0].set_xlabel("step no. $\\rightarrow$" )
ax[0,0].set_ylabel("step value $\\rightarrow$")

ax[0,1].hist(seeds,weights=collatz_lengths,bins=range(2,m+2),color="green")
ax[0,1].text(point+1,max(collatz_lengths)+2,f"maximum steps= {max(collatz_lengths)} at {point} ")
ax[0,1].set_title("Collatz_length of series of numbers")
ax[0,1].set_xlabel("seed no. $\\rightarrow$" )
ax[0,1].set_ylabel("Collatz Length $\\rightarrow$")

ax[1,0].hist(step,weights=frequency,bins=range(1,max(step)+1))
ax[1,0].set_title(f"Frequency distribution upto {m}")
ax[1,0].text(most_step+4,maxf,f"most probable steps= {most_step} of frequency= {maxf}")
ax[1,0].set_xlabel("no. of steps $\\rightarrow$" )
ax[1,0].set_ylabel("Frequency $\\rightarrow$")
plt.show()