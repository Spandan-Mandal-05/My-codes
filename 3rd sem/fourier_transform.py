#Fourier Transform
import numpy as np
import matplotlib.pyplot as plt
from mpl_toolkits import mplot3d

#define Transform coefficients & x axis values
ks = np.linspace(-20,20,2000)
xx = ks

#define the function 
def f(x):
	#return np.where((-1<=x)&(x<=0),1+x,np.where((0<=x)&(x<=1),1-x,0))
	#return np.sin(np.log(5*x**2+3))+np.cos(np.log(5*x**2+3))
	return (0.8*np.sin(x) - 0.4*np.sin(5*x) + 0.6*np.sin(7*x) - 0.4*np.sin(17*x) + 0.7*np.sin(3*x))
	#return np.where((x<0),0,1)

#real functional values
xxs = f(xx)

#define & separate odd & even functions' transform 
def if_even_function(f, x, tol=1e-5):
    return np.all(np.abs(f(x) - f(-x)) < tol)
def if_odd_function(f, x, tol=1e-5):
    return np.all(np.abs(f(x) + f(-x)) < tol)

if if_even_function(f,xx):
	# Apply the cosine Fourier transform for even function
	gks = [(2*np.pi)**(-0.5) * np.trapz(f(xx)*np.cos(k*xx),xx) for k in ks ]

	fig,axs = plt.subplots(2,2,figsize=(12,8),layout="constrained")

	gs = axs[0,0].get_gridspec()
	for ax in axs[0,:]:
		ax.remove()
	ax1 = fig.add_subplot(gs[0,:])
	ax2 = axs[1,0]
	ax3 = axs[1,1]


	ax1.plot(ks,gks,color='black',label="fourier transform of f(x) = F(k)")
	ax1.plot(xx,xxs,'-',color='black',alpha=0.6,label="f(x)")
	ax1.legend(loc="best",fontsize=12)
	ax1.grid(True)
	ax1.set_xlabel(" x or k $\\rightarrow$")
	ax1.set_ylabel(" f(x) or |F(k)| $\\rightarrow$")
	ax1.axvline(0,linestyle="--",color='black',alpha=0.5)
	ax1.axhline(0,linestyle="--",color='black',alpha=0.5)

	#ax2.plot(ks,gks,color='black',label="fourier transform of f(x) = F(k)")
	ax2.plot(xx,xxs,'-',color='black',alpha=1,label="f(x)")
	ax2.legend(loc="best",fontsize=12)
	ax2.grid(True)
	ax2.set_xlabel(" x $\\rightarrow$")
	ax2.set_ylabel(" f(x) $\\rightarrow$")
	ax2.axvline(0,linestyle="--",color='black',alpha=0.5)
	ax2.axhline(0,linestyle="--",color='black',alpha=0.5)

	ax3.plot(ks,gks,color='black',label="fourier transform of f(x) = F(k)")
	#ax2.plot(xx,xxs,'--',color='black',alpha=1,label="f(x)")
	ax3.legend(loc="best",fontsize=12)
	ax3.grid(True)
	ax3.set_xlabel(" k $\\rightarrow$")
	ax3.set_ylabel(" |F(k)| $\\rightarrow$")
	ax3.axvline(0,linestyle="--",color='black',alpha=0.5)
	ax3.axhline(0,linestyle="--",color='black',alpha=0.5)

	plt.show()
	exit()

if if_odd_function(f,xx):
	# Apply the sine Fourier transform for odd function
	gks = [(2*np.pi)**(-0.5) * np.trapz(f(xx)*np.sin(k*xx),xx) for k in ks ]

	fig,axs = plt.subplots(2,2,figsize=(12,8),layout="constrained")

	gs = axs[0,0].get_gridspec()
	for ax in axs[0,:]:
		ax.remove()
	ax1 = fig.add_subplot(gs[0,:])
	ax2 = axs[1,0]
	ax3 = axs[1,1]


	ax1.plot(ks,gks,color='black',label="fourier transform of f(x) = F(k)")
	ax1.plot(xx,xxs,'-',alpha=0.6,color='black',label="f(x)")
	ax1.legend(loc="best",fontsize=12)
	ax1.grid(True)
	ax1.set_xlabel(" x or k $\\rightarrow$")
	ax1.set_ylabel(" f(x) or |F(k)| $\\rightarrow$")
	ax1.axvline(0,linestyle="--",color='black',alpha=0.5)
	ax1.axhline(0,linestyle="--",color='black',alpha=0.5)

	#ax2.plot(ks,gks,color='black',label="fourier transform of f(x) = F(k)")
	ax2.plot(xx,xxs,color='black',label="f(x)")
	ax2.legend(loc="best",fontsize=12)
	ax2.grid(True)
	ax2.set_xlabel(" x $\\rightarrow$")
	ax2.set_ylabel(" f(x) $\\rightarrow$")
	ax2.axvline(0,linestyle="--",color='black',alpha=0.5)
	ax2.axhline(0,linestyle="--",color='black',alpha=0.5)

	ax3.plot(ks,gks,color='black',label="fourier transform of f(x) = F(k)")
	#ax2.plot(xx,xxs,'--',color='black',alpha=1,label="f(x)")
	ax3.legend(loc="best",fontsize=12)
	ax3.grid(True)
	ax3.set_xlabel(" k $\\rightarrow$")
	ax3.set_ylabel(" |F(k)| $\\rightarrow$")
	ax3.axvline(0,linestyle="--",color='black',alpha=0.5)
	ax3.axhline(0,linestyle="--",color='black',alpha=0.5)

	plt.show()
	exit()

else : 
	# For general non-symmetric functions
	gks_cos = [(2*np.pi)**(-0.5) * np.trapz(f(xx)*np.cos(k*xx),xx) for k in ks ]
	gks_sine = [(2*np.pi)**(-0.5) * np.trapz(f(xx)*np.sin(k*xx),xx) for k in ks ]
	gks = np.array(gks_cos)+ 1j * np.array(gks_sine)
	mod_gks = np.sqrt(np.square(gks_cos) + np.square(gks_sine))

	
	fig,axs = plt.subplots(2,2,figsize=(12,8),layout="constrained")

	gs = axs[0,0].get_gridspec()
	for ax in axs[0,:]:
		ax.remove()
	ax1 = fig.add_subplot(gs[0,:])
	ax2 = axs[1,0]
	ax3 = axs[1,1]


	ax1.plot(ks,gks,color='black',label="fourier transform of f(x) = F(k)")
	ax1.plot(xx,xxs,'-',alpha=0.6,color='black',label="f(x)")
	ax1.legend(loc="best",fontsize=12)
	ax1.grid(True)
	ax1.set_xlabel(" x or k $\\rightarrow$")
	ax1.set_ylabel(" f(x) or |F(k)| $\\rightarrow$")
	ax1.axvline(0,linestyle="--",color='black',alpha=0.5)
	ax1.axhline(0,linestyle="--",color='black',alpha=0.5)

	#ax2.plot(ks,gks,color='black',label="fourier transform of f(x) = F(k)")
	ax2.plot(xx,xxs,'-',color='black',alpha=1,label="f(x)")
	ax2.legend(loc="best",fontsize=12)
	ax2.grid(True)
	ax2.set_xlabel(" x $\\rightarrow$")
	ax2.set_ylabel(" f(x) $\\rightarrow$")
	ax2.axvline(0,linestyle="--",color='black',alpha=0.5)
	ax2.axhline(0,linestyle="--",color='black',alpha=0.5)

	ax3.plot(ks,gks,color='black',label="fourier transform of f(x) = F(k)")
	#ax2.plot(xx,xxs,'--',color='black',alpha=1,label="f(x)")
	ax3.legend(loc="best",fontsize=12)
	ax3.grid(True)
	ax3.set_xlabel(" k $\\rightarrow$")
	ax3.set_ylabel(" |F(k)| $\\rightarrow$")
	ax3.axvline(0,linestyle="--",color='black',alpha=0.5)
	ax3.axhline(0,linestyle="--",color='black',alpha=0.5)

	plt.show()
	exit()


	fig = plt.figure()
	ax = plt.axes(projection = "3d")
	# Prepare data for the surface plot
	K, G = np.meshgrid(ks, ks)  # Create meshgrid for k values
	Z = np.outer(np.real(gks), np.imag(gks))  # Create Z as the outer product of real and imaginary parts

	ax.plot_surface( K, G, Z,cmap='viridis',\
                edgecolor='green', label="Fourier transform of f(x)")
	# Adding labels
	ax.set_xlabel('k values')
	ax.set_ylabel('Real part of gks')
	ax.set_zlabel('Imaginary part of gks')

	#ax.plot(xx,xxs,label="real function")
	#ax.plot(xx,uncertainty,label="uncertainty")
	plt.legend(loc="best")
	ax.grid(True)
	plt.show()
	exit()

