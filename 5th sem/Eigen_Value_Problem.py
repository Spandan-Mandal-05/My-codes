# Shooting Method for Eigen Value Problem
import matplotlib.pyplot as plt
import numpy as np
import time

# Define Potential
def V(x):
    #L = 2  # Width of the potential well
    #return np.where((x >= -L/2) & (x <= L/2), 0, 1e6) # Free Particle

    w = 1  # Frequency for Harmonic Oscillator
    return 0.5 * w**2 * x**2  # Harmonic Oscillator Potential

# Define Differential Eq
def d2y_dx2(x, y, g, E):
    mass = 1 # Mass of the particle
    h_cut = 1 # Planck's constant
    return  (V(x) - E) * y * 2 * mass / h_cut**2
    #return -2*E*y  # E = Energy Eigen Value 

# Define the ODE solver using the Shooting Method
def sol_ode(initial_state, boundary_state, E):
    n = 10000
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
xi, xf = -5, 5
yi, yf = 0, 0

# Initial guesses for y'(0)
gg_shoot = 2

# Plot setup
fig, ax = plt.subplots(figsize=[12, 8])

# Start timing
start_time = time.time()

Energys = np.linspace(0.49,2.6,1000)
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

roots = []
for i in range(len(Energys)-1):
    if y_finals[i] * y_finals[i+1] < 0:
        roots.append((Energys[i] + Energys[i+1]) / 2)
print("Eigen energies ≈", np.round(roots,2))
E_n = np.round(roots,2)

# Plot setup
fig, ax = plt.subplots(figsize=[12, 8])

xx, yy_modified, y_boundary_i = sol_ode((xi, yi, gg_shoot), xf, 1.5)
plt.plot(xx, V(xx), color="red", alpha=0.6, label="Potential  V(x)")

# Normalize y(x)
norm = np.trapz(yy_modified**2, xx)**0.5
yy_norm = yy_modified / norm

# Plot potential and scaled wavefunction
plt.plot(xx, yy_norm**2+1.5 , label="Normalized wavefunction")
#plt.plot(xx, V(xx)/10, label="Potential V(x)/10")  # divide by 10 to fit same scale
plt.legend()

"""                                 
# Initial guesses for y'(0)
gg_shoot_i = 1
gg_shoot_f = 2



# Initial two trial solutions
xx, yy_modified, y_boundary_i = sol_ode((xi, yi, gg_shoot_i), xf, E_n[1])
plt.plot(xx, 2*yy_modified, color="black", alpha=0.6)
xx, yy_modified, y_boundary_f = sol_ode((xi, yi, gg_shoot_f), xf, E_n[1])
plt.plot(xx, yy_modified, color="black", alpha=0.2)


# Error at boundary
error_i = yf - y_boundary_i
error_f = yf - y_boundary_f
tolerance = 1e-6

# Shooting method iteration
while abs(error_f - error_i) >= tolerance:
    if error_i * error_f < 0:
        c = (gg_shoot_i + gg_shoot_f) / 2
        xx, yy_modified, y_boundary_c = sol_ode((xi, yi, c), xf, E_n[0])
        plt.plot(xx, yy_modified, color="black", alpha=0.2)

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
xx, yy_modified, _ = sol_ode((xi, yi, c), xf, E_n[0])

# Plot numerical and analytical solutions
plt.plot(xx, yy_modified, color="blue", linewidth=2, label=f"Shooting Method (g = {c:.6f})")

plt.xlabel("x")
plt.ylabel("y(x)")
plt.title("Shooting Method vs Analytical")
plt.legend()
plt.grid(True) """
plt.show()