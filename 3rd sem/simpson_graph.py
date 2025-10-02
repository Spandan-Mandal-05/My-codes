import matplotlib.pyplot as plt
import numpy as np

# Define the function to be integrated: f(x) = e^(-x^2)
def f(x):
    return np.exp(-x**2)

# Simpson's Rule integration function for a given number of points `n`
def intg(n):
    x = -6                
    xf = 6              
    g, m = 0, 0           
    h = (xf - x) / (n - 1)  
    yy = []               

    # Compute function values at each x, storing in yy
    for k in range(n):
        y = f(x)
        yy.append(y)
        x = x + h
    
    # Apply Simpson's Rule: Sum odd and even indexed terms
    for j in range(n // 2):
        g = g + 4 * yy[2 * j + 1]    # Sum of terms with odd indices
        if 2 * j + 2 < (n - 1):
            m = m + 2 * yy[2 * j + 2]  # Sum of terms with even indices

    # Complete Simpson's formula for integral approximation
    s = h / 3 * (yy[0] + g + m + yy[n - 1])
    return s 

# Convergence Analysis: Iteratively increase n until error threshold is met
n = 3                         # Initial number of points
integral_1, nn = [], []      
r = 1e-3                      # approximation error

# Convergence based on the error threshold
while abs(intg(n + 2) - intg(n)) >= r:
    integral_1.append(intg(n))
    nn.append(n)
    n += 2

# Plot of Integral vs. Number of Points (Convergence Analysis)
fig, ax = plt.subplots(2, 1, figsize=(8, 10), constrained_layout=True)

# First Plot: Convergence of Integral with Increasing Points
ax[0].plot(nn, integral_1, 'o-', color='black', label='Approx. Integral')
ax[0].axhline(y=np.sqrt(np.pi), color='black', alpha=0.5, linestyle='--', label='Theoretical $\\sqrt{\\pi}$')
ax[0].axvline(x=max(nn), color='black', alpha=0.5, linestyle=':', label=f"Max points = {max(nn)} for error limit {r}")
ax[0].grid(True)
ax[0].set_ylabel("Integral Value $\\rightarrow$")
ax[0].set_xlabel("Number of Points $n \\rightarrow$")
ax[0].set_title("Convergence of Integral $e^{-x^2}$ with Increasing Points")
ax[0].legend()
ax[0].text(max(nn) * 0.7, 3, f"Convergence achieved within $r={r}$", fontsize=9, color='black')

# Simpson's Rule for varying interval sizes
def intg(x):
    xi = -x                   # Start of the interval
    xf = x                    # End of the interval
    n = 1001                  # Fixed number of points for high accuracy
    g, m = 0, 0               # Initialize sums for odd and even indexed terms
    h = (xf - xi) / (n - 1)   # Step size for Simpson's method
    yy = []                   # List to store function values

    # Compute function values at each x, storing in yy
    for k in range(n):
        y = f(xi)
        yy.append(y)
        xi = xi + h
    
    # Apply Simpson's Rule: Sum odd and even indexed terms
    for j in range(n // 2):
        g = g + 4 * yy[2 * j + 1]    # Sum of terms with odd indices
        if 2 * j + 2 < (n - 1):
            m = m + 2 * yy[2 * j + 2]  # Sum of terms with even indices

    # Complete Simpson's formula for integral approximation
    s = (h / 3) * (yy[0] + g + m + yy[n - 1])
    return s 

# Interval Analysis: Compute integral for increasing interval lengths
x = 0.25                   # Starting interval size
integral_2, xx = [], []    

# increase interval size and calculate integral
while x <= 4:
    integral_2.append(intg(x))
    xx.append(2 * x)
    x += 0.125

# Second Plot: Integral vs. Interval Length (Xf - Xi)
ax[1].plot(xx, integral_2, 'o-', color='black', label="Approx. Integral over Interval")
ax[1].axhline(y=np.sqrt(np.pi), color='black', alpha=0.5, linestyle='--', label="Theoretical $\\sqrt{\\pi}$")
ax[1].grid(True)
ax[1].set_ylabel("Integral Value over Interval $\\rightarrow$")
ax[1].set_xlabel("Interval Length $(X_f - X_i) \\rightarrow$")
ax[1].set_title("Integral of $e^{-x^2}$ over Varying Interval Lengths")
ax[1].legend()
ax[1].text(4, 1, f"No of Points = {n}", fontsize=9, color='black')

# Display the plots
plt.show()