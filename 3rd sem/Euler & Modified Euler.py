# Import Libraries
import matplotlib.pyplot as plt 
import numpy as np

# Differential Equation
def d2y_dx2(x, y, g):
    return 14 * x**2 - 2 + 4 * y - x * g 

# Analytical Solution
def f(x):
    return x**4 - x**2

# Solve ODE with Euler and Modified Euler
def sol_ode(initial_state, step_no, end): 
    n = step_no
    xi, yi, gi = initial_state
    xf = end
    h = (xf - xi) / (n - 1)
    xx = np.linspace(xi, xf, n)
    yy = f(xx)
    
    # Initialize solutions
    yy_modified = np.zeros_like(xx)
    gg_modified = np.zeros_like(xx)
    yy_e = np.zeros_like(xx)
    gg_e = np.zeros_like(xx)

    # Set boundary values
    gg_e[0], yy_e[0] = gi, yi
    gg_modified[0], yy_modified[0] = gi, yi

    for i in range(n - 1):
        # Euler Method
        gg_e[i+1] = gg_e[i] + h * d2y_dx2(xx[i], yy_e[i], gg_e[i])
        yy_e[i+1] = yy_e[i] + h * gg_e[i+1]

        # Modified Euler Method
        g_temp = gg_modified[i] + h * d2y_dx2(xx[i], yy_modified[i], gg_modified[i])
        y_temp = yy_modified[i] + h * gg_modified[i]
        gg_modified[i+1] = gg_modified[i] + h * 0.5 * (d2y_dx2(xx[i], yy_modified[i], gg_modified[i]) + d2y_dx2(xx[i+1], y_temp, g_temp))
        yy_modified[i+1] = yy_modified[i] + h * 0.5 * (gg_modified[i] + g_temp)

    return xx, yy, yy_e, yy_modified

# Initial boundary condition
State0 = (-1, 0, -2) 

# Set error and steps
error, t, i = 0.1, 10, 0  
xx, yy, yy_e, yy_modified = sol_ode(State0, t, 0.25)
tt, Real_max, Euler_max, Modified_max = [], [], [], []

# Convergence loop
while abs(yy_e[np.argmax(xx)] - yy[np.argmax(xx)]) >= error or abs(yy_modified[np.argmax(xx)] - yy[np.argmax(xx)]) >= error:
    tt.append(t)
    Real_max.append(yy[np.argmax(xx)]) 
    Euler_max.append(yy_e[np.argmax(xx)])
    Modified_max.append(yy_modified[np.argmax(xx)])
    t += 5
    xx, yy, yy_e, yy_modified = sol_ode(State0, t, 0.25)

# Final solution with extended steps
xx, yy, yy_e, yy_modified = sol_ode(State0, 300, 1) 

# Plot solutions and convergence
fig, ax = plt.subplots(2, 1, figsize=(10, 8), constrained_layout=True)

# Solution plot
ax[0].plot(xx, yy, '-', color='black', label="Analytical")
ax[0].plot(xx, yy_e, '-.', color='black', alpha=0.65, label="Euler")
ax[0].plot(xx, yy_modified, '--', color='black', alpha=0.85, label="Modified Euler")
ax[0].set_ylabel("f(x) $\\rightarrow$")
ax[0].set_xlabel("x $\\rightarrow$")
ax[0].axhline(y=0, color='black', alpha=0.45)
ax[0].axvline(x=0, color='black', alpha=0.45)
ax[0].set_title("Solution of $\\frac{d^2y}{dx^2}$ + 2$\\frac{dy}{dx}$ + 5y = 0 (y vs x)")
ax[0].grid(True, alpha=0.35)
ax[0].legend(loc="best")

# Convergence plot
ax[1].plot(tt, Real_max, ':', color='black', label="Analytical")
ax[1].plot(tt, Euler_max, '-.', color='black', alpha=0.65, label="Euler")
ax[1].plot(tt, Modified_max, '--', color='black', alpha=0.85, label="Modified Euler")
ax[1].set_ylabel("f(0.25)")
ax[1].set_xlabel("Number of Steps")
ax[1].set_title("Convergence of Analytical Value")
ax[1].grid(True, alpha=0.35)
ax[1].legend(loc="best")

plt.show()
