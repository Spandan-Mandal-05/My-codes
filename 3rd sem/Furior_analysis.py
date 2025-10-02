# Fourier Analysis for f(x)
import matplotlib.pyplot as plt
import numpy as np

# Initialize parameters
pi = np.pi
xi = -1  # Lower limit of the period
xf = 1   # Upper limit of the period
L = (xf - xi)  # Period length
n = 300   # Number of terms in Fourier Series
npt = 10**5 + 1  # Number of steps for integration
h = (xf - xi) / (npt - 1)  # Step size

# Define the original function
def f(x):
    return x

# Define sine and cosine terms for Fourier series
def sin_i(i, x):
    return np.sin((2 * pi / L) * i * x)

def cos_i(i, x):
    return np.cos((2 * pi / L) * i * x)

# Initialize Fourier coefficients
aa, bb = np.zeros(n + 1), np.zeros(n + 1)
xx = np.linspace(xi, xf, npt)  # Points for integration

# Compute Fourier coefficients using numerical integration (trapezoidal rule)
for i in range(n + 1):
    aa[i] = np.trapz(cos_i(i, xx) * f(xx), xx) / (L / 2)  # Coefficients for cosine terms
    bb[i] = np.trapz(sin_i(i, xx) * f(xx), xx) / (L / 2)  # Coefficients for sine terms

# Define the complete Fourier series as a function
def fn(x):
    g = aa[0] / 2  # Constant term (a_0/2)
    for i in range(1, n + 1):
        g += aa[i] * np.cos((2 * pi / L) * i * x) + bb[i] * np.sin((2 * pi / L) * i * x)
    return g

# Generate data for plotting
xx1 = np.linspace(xi, 5 * xf, npt)  # Extended range for Fourier approximation
yy1 = fn(xx1)  # Fourier approximation values
xx2 = np.linspace(1.5 * xi, 1.5 * xf, npt)  # Range for original function
yy2 = f(xx2)  # Original function values

# Plot the results
plt.plot(xx1, yy1, color='black', label="Fourier Approximation of f(x)")  # Fourier series approximation
plt.plot(xx2, yy2, '--', color='black', label="Real Function", alpha=0.7)  # Original function
plt.xlabel("x $\\rightarrow$")  # Label for x-axis
plt.ylabel("f(x) $\\rightarrow$")  # Label for y-axis
plt.axvline(x=0, color='black', alpha=0.5)  # Vertical axis
plt.axhline(y=0, color='black', alpha=0.5)  # Horizontal axis
plt.grid(True, alpha=0.8, ls=':')  # Grid with dashed lines
plt.title("Fourier Series")  # Title of the plot
plt.legend(loc="best")  # Legend positioning
plt.show()



