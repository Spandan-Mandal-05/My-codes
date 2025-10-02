import matplotlib.pyplot as plt 
fig,axs = plt.subplots(2,2,figsize=(12,8))
gs = axs[0,0].get_gridspec()
for ax in axs[0,:]:
    ax.remove()

ax1 = fig.add_subplot(gs[0,:])
fig.tight_layout()
plt.show()