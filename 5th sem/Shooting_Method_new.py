# Shooting Method using Bisection
import matplotlib.pyplot as plt
import numpy as np
import time

# Define Differential Eq
def d2y_dx2(x, y, g):
    return np.sin(x) - 4*y

#Define Analytical Eq
def f(x):
    return -np.sin(1)/(3*np.sin(2)) * np.sin(2*x) + np.sin(x)/3

# Define the ODE solver using the Shooting Method
def sol_ode(initial_state, boundary_state):
    n = 50000
    xf = boundary_state
    xi, yi, gi = initial_state
    h = (xf - xi) / (n - 1)

    xx = np.linspace(xi, xf + h, n + 1)
    yy = f(xx)

    yy_modified = np.zeros_like(xx)
    gg_modified = np.zeros_like(xx)

    yy_modified[0], gg_modified[0] = yi, gi

    for i in range(n):
        gg_temp = gg_modified[i] + h * d2y_dx2(xx[i], yy_modified[i], gg_modified[i])
        yy_temp = yy_modified[i] + h * gg_temp

        gg_modified[i + 1] = gg_modified[i] + h / 2 * (d2y_dx2(xx[i + 1], yy_temp, gg_temp) + d2y_dx2(xx[i], yy_modified[i], gg_modified[i]))
        yy_modified[i + 1] = yy_modified[i] + h / 2 * (gg_modified[i] + gg_temp)

        #gg_modified[i+1] = gg_modified[i] + h * d2y_dx2(xx[i], yy_modified[i], gg_modified[i])
        #yy_modified[i+1] = yy_modified[i] + h * gg_modified[i+1]

    y_boundary = yy_modified[n]
    return xx, yy, yy_modified, y_boundary

# Boundary conditions
xi, xf = 0, 1
yi, yf = 0, 0

# Initial guesses for y'(0)
gg_shoot_i = -10
gg_shoot_f = 5

# Plot setup
fig, ax = plt.subplots(figsize=[12, 8])

# Initial two trial solutions
xx, yy, yy_modified, y_boundary_i = sol_ode((xi, yi, gg_shoot_i), xf)
plt.plot(xx, yy_modified, color="black", alpha=0.5)
xx, yy, yy_modified, y_boundary_f = sol_ode((xi, yi, gg_shoot_f), xf)
plt.plot(xx, yy_modified, color="black", alpha=0.5)

# Error at boundary
error_i = yf - y_boundary_i
error_f = yf - y_boundary_f
tolerance = 1e-6

# Start timing
start_time = time.time()

# Shooting method iteration and bisection
while abs(error_f - error_i) >= tolerance:
    if error_i * error_f < 0:
        c = (gg_shoot_i + gg_shoot_f) / 2
        xx, yy, yy_modified, y_boundary_c = sol_ode((xi, yi, c), xf)
        plt.plot(xx, yy_modified, color="black", alpha=0.5)

        error_c = yf - y_boundary_c

        if error_c * error_f < 0:
            gg_shoot_i = c
            error_i = error_c
        elif error_c * error_i < 0:
            gg_shoot_f = c
            error_f = error_c
        else:
            print("Converged or undefined behavior")
            break


# Final solution
xx, yy, yy_modified, _ = sol_ode((xi, yi, c), xf)

# End timing
end_time = time.time()
elapsed_time = end_time - start_time
print(f"Final Shooting Method Run Time: {elapsed_time:.4f} seconds")

# Plot numerical and analytical solutions
plt.plot(xx, yy_modified, color="blue", linewidth=2,
         label=f"Shooting Method: g = {c:.6f}, y({xf}) = {yy_modified[-1]:.6f}")

plt.plot(xx, yy, '--', color="red", label="Analytical Solution")

plt.xlabel("x")
plt.ylabel("y(x)")
plt.title("Shooting Method vs Analytical")
plt.legend()
plt.grid(True)
plt.show()

