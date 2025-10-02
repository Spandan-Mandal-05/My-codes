import matplotlib.pyplot as plt
import numpy as np

# Constants
pi = np.pi
xi = -1  # Lower limit of the period
xf = 1   # Upper limit of the period
L = (xf - xi)  # Period
npt = 10**4+1    # Number of steps for integration
h = (xf - xi) / (npt - 1)

# Define the original function
def f(x):
    return np.where((x >= 0), 1, -1)

# Define sine & cosine terms
def sin_i(i, x):
    return np.sin((2 * pi / L) * i * x)

def cos_i(i, x):
    return np.cos((2 * pi / L) * i * x)

# Define Fourier series as a function
def fourier(mode, n, f):
    aa, bb = np.zeros(n + 1), np.zeros(n + 1)
    xx1 = np.linspace(xi, xf, npt)

    # Calculating the coefficients for the Fourier series
    for i in range(n + 1):
        aa[i] = np.trapz(cos_i(i, xx1) * f(xx1), xx1) / (L / 2) 
        bb[i] = np.trapz(sin_i(i, xx1) * f(xx1), xx1) / (L / 2)
		
	# Creating the Fourier series function
    def fn(x):
        g = aa[0] / 2
        g += np.sum([aa[i] * cos_i(i, x) + bb[i] * sin_i(i, x) for i in range(1, n + 1)], axis=0)
        return g

    xx2 = np.linspace(xf/2, xf, npt)
    yy1 = fn(xx2)

    # Modes: 0 - x position of overshoot, 1 - overshoot value, 2 - plot the Fourier series
    if mode == 0:
        return xx2[np.argmax(yy1)]
    elif mode == 1:
        return abs(max(yy1) - 1)
    elif mode == 2:
        return xx2,yy1
# Fourier series analysis
nn = np.arange(1,100, 2)  # Number of terms in Fourier series

xx = [fourier(0, n, f) for n in nn]  # x position of overshoot for different Fourier terms
yy = [fourier(1, n, f) for n in nn]  # Overshoot value for different Fourier terms

# Plotting the Fourier series
nn1 = np.arange(5, 100, 30)  # Number of terms in Fourier series
alphas = [0.2,0.3,0.6,1]

for alpha,n in zip(alphas,nn1):
    xx2, yy1 = fourier(2, n, f)
    plt.plot(xx2, yy1, alpha=alpha, color='black', label=f"Fourier Series for {n} terms")

plt.legend(loc="best")
plt.grid(True)
plt.xlabel("x $\\rightarrow$")
plt.ylabel("f(x) $\\rightarrow$")
plt.show()

# Plotting the overshoot characteristics
fig, ax = plt.subplots(2,1, figsize=(8, 8), constrained_layout=True)

ax[0].plot(nn, xx, '-o',color='black', label=f"Min overshoot: {min(yy):.5f} at x = {xx[np.argmin(yy)]:.5f} for {nn[np.argmin(yy)]} Fourier terms")
ax[0].grid(True)
ax[0].set_ylabel("Overshoot x position $\\rightarrow$")
ax[0].set_xlabel("Fourier Terms $\\rightarrow$")
ax[0].legend(loc="best")

ax[1].plot(nn, yy, '-*',color='black', label=f"Min overshoot value: {min(yy):.5f} at x = {xx[np.argmin(yy)]:.5f} for {nn[np.argmin(yy)]} Fourier terms")
ax[1].grid(True)
ax[1].set_ylabel("Overshoot value $\\rightarrow$")
ax[1].set_xlabel("Fourier Terms $\\rightarrow$")
ax[1].legend(loc="best")

plt.show()



