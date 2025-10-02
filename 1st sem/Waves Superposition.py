import matplotlib.pyplot as plt
import numpy as np
from matplotlib import animation 
#from matplotlib.animation import PillowWriter

fig, ax=plt.subplots()
t=np.linspace(0,8*np.pi,10000)
a=3
omega=30
x=a*np.cos(t)
y=a*np.sin(t)
ax.arrow(0, 0, a, 0,
          length_includes_head=True,
          width=0.01,
          edgecolor='black',
          facecolor='green',
          lw=2,
          zorder=2)
ax.set_xlim(-4,4)
ax.set_ylim(-4,4)

def animate(i):
    ax.cla() # clear the current axes
    circle = plt.Circle((0, 0), 3, edgecolor='#666600', fill=False)
    ax.add_patch(circle) # add the circle patch to the axes
    ax.arrow(0, 0, x[omega*i], y[omega*i],
          length_includes_head=True,
          width=0.01,
          edgecolor='black',
          facecolor='green',
          lw=2,
          zorder=2)
    ax.arrow(0, 0, 0, y[omega*i],
          length_includes_head=True,
          width=0.01,
          edgecolor='red',
          facecolor='green',
          lw=2,
          zorder=2)
    ax.arrow(0, 0, x[omega*i], 0,
          length_includes_head=True,
          width=0.01,
          edgecolor='#3300FF',
          facecolor='green',
          lw=2,
          zorder=2)
    sin,=ax.plot(t[:omega*i],a*np.sin(t[:omega*i]+t[omega*i]),color='#7B1FA2') 
    ax.set_xlim(-4,7)
    ax.set_ylim(-4,4)
    ax.set_aspect('equal')
    ax.grid(True,alpha=0.3)
    ax.legend([sin],['$asin(\\omega t)$'])
    ax.set_xlabel("real-axis",fontstyle="oblique")
    ax.set_ylabel("imaginary-axis",fontstyle="oblique")
    ax.set_title('Phasor',fontname='Copperplate Gothic Light',fontsize=20)

ani=animation.FuncAnimation(fig,animate,frames=120,interval=50)
plt.show()