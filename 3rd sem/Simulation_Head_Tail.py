#Simulation of Coin Toissing
import numpy as np
import matplotlib.pyplot as plt

def toss(mode):
    xx=np.random.random(size=(n))
    Head,Tail=np.zeros(n),np.zeros(n)
    for i in range (n):
        if 0<=xx[i]<0.5: Head[i]=1 #define Heads
        elif 0.5<=xx[i]<1 : Tail[i]=1 #define Tails
    if mode == 0:
        return int(np.sum(Head))  # Count total heads
    elif mode == 1:
        return int(np.sum(Tail))  # Count total tails
    
n=100 #Number of Coin Tossing
avg_H = []
expt = 0
nex =  10000 #No. of Repetation of the Experiment
for i in range(nex):
    expt += toss(0)
    avg_H.append((expt)/(i+1))
plt.plot(np.arange(1,nex+1,1),avg_H,'-',color='black')
plt.axhline(y=n/2)
plt.xlim(-20)
plt.xlabel('Experiment Number $\\rightarrow$')
plt.ylabel('Average(Heads) $\\rightarrow$')
plt.grid(True)
plt.title('Simulating Coin Tossing')
plt.show()
