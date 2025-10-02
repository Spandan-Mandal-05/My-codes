# Shooting Method for Eigen Value Problem
import matplotlib.pyplot as plt
import numpy as np
import time #To measure the time taken for execution
import scipy.special as sp

# Define Differential Eq
def d2y_dx2(x, y, g, E):
    return -2*E*y  # E = Energy Eigen Value 

# Define the ODE solver using the Shooting Method
def sol_ode(initial_state, boundary_state, E):
    n = 5000
    xf = boundary_state
    xi, yi, gi = initial_state
    h = (xf - xi) / (n - 1)

    xx = np.linspace(xi, xf + h, n + 1)

    yy_modified = np.zeros_like(xx)
    gg_modified = np.zeros_like(xx)

    yy_modified[0], gg_modified[0] = yi, gi

    for i in range(n):
        gg_temp = gg_modified[i] + h * d2y_dx2(xx[i], yy_modified[i], gg_modified[i], E)
        yy_temp = yy_modified[i] + h * gg_temp

        gg_modified[i + 1] = gg_modified[i] + h / 2 * (d2y_dx2(xx[i + 1], yy_temp, gg_temp, E) + d2y_dx2(xx[i], yy_modified[i], gg_modified[i], E))
        yy_modified[i + 1] = yy_modified[i] + h / 2 * (gg_modified[i] + gg_temp)

        #gg_modified[i+1] = gg_modified[i] + h * d2y_dx2(xx[i], yy_modified[i], gg_modified[i])
        #yy_modified[i+1] = yy_modified[i] + h * gg_modified[i+1]

    y_boundary = yy_modified[n]
    return xx, yy_modified, y_boundary

# Boundary conditions
xi, xf = 0, 1
yi, yf = 0, 0

# Initial guesses for y'(0)
gg_shoot = 0.5

# Plot setup
fig, ax = plt.subplots(figsize=[12, 8])

# Start timing
start_time = time.time()

Energys = np.linspace(0,100,10000)
y_finals = [sol_ode((xi,yi,gg_shoot),xf, E)[2] for E in Energys]

# End timing
end_time = time.time()
elapsed_time = end_time - start_time
print(f"Final Shooting Method Run Time: {elapsed_time:.4f} seconds")

# Plot numerical and analytical solutions
plt.plot(Energys, y_finals)
plt.xlabel("Energy Eigen Value (E)")
plt.ylabel("y(1)")
plt.title("Shooting Method for Eigen Value Problem")
plt.legend()
plt.grid(True)
plt.show()
