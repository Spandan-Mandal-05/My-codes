import matplotlib.pyplot as plt
import numpy as np
from scipy.integrate import simpson

# Function definition
def f(x, y):
    return np.ones_like(y)  # Return an array of ones matching y's shape

# Fourier trick function
def fourier_trick(n, f, a=1):
    pi = np.pi  # Define pi locally
    yy = np.linspace(0, a, 1000)  # Create the y-axis grid for integration

    b_n = [(2 / a) * simpson(f(0, yy) * np.sin(k * pi * yy / a), x=yy) for k in range(1, n + 1)]


    # Define a function that computes V(x, y) using the precomputed b_n
    def V(x, y):
        return sum(
            b_n[k - 1] * np.cosh(k * pi * x / a) * np.sin(k * pi * y / a)
            for k in range(1, n + 1)
        )

    return V

# Constants
pi = np.pi
a = 1  # Period length
b = 1
n = 100  # Number of Fourier terms

# Precompute the Fourier series
V = fourier_trick(n, f, a)

# Plot the Fourier series for a range of y with fixed x
yy = np.linspace(0, a, 500)  # Define y values
xx = np.linspace(-b, b, 500)  # Fixed x value
X , Y = np.meshgrid(xx, yy)
Z = V(X, Y)

# plot
fig, ax = plt.subplots()

ax.pcolormesh(X, Y, Z, vmin=-0.5, vmax=1.0)

#plt.plot(yy1, [V(x, y) for y in yy1], label=f"n={n}")
#plt.title("Fourier Series Approximation")
#plt.xlabel("y")
#plt.ylabel("V(y)")
#plt.grid(True)
#plt.legend()
plt.show()









