# =============================================================
#  SHOOTING METHOD FOR EIGENVALUE PROBLEM
#  Author: Spandy
#  Description:
#     This code numerically finds eigenenergies and wavefunctions
#     for 1D quantum systems using the Shooting Method.
# =============================================================

import matplotlib.pyplot as plt
import numpy as np
import time

# =============================================================
# 1. DEFINE POTENTIAL FUNCTION V(x)
# -------------------------------------------------------------
# You can modify this section to change the potential.
# Examples:
#   - Infinite Square Well
#   - Finite Well
#   - Harmonic Oscillator (default)
# =============================================================
def V(x):
    # Uncomment one of the following potentials
    
    # --- Infinite Square Well ---
    # L = 2
    # return np.where((x >= -L/2) & (x <= L/2), 0, 1e6)

    # --- Finite Square Well ---
    # V0 = 5.0   # Depth of the well
    # L = 2.0    # Width of the well
    # return np.where(np.abs(x) <= L/2, -V0, 0.0)

    # --- Finite Barrier (Rectangular Barrier) ---
     V0 = 5.0   # Height of the barrier
     L = 2.0    # Width of the barrier
     return np.where(np.abs(x) <= L/2, V0, 0.0)

    # --- Harmonic Oscillator (default) ---
    #w = 1  # Frequency ω
    #return 0.5 * w**2 * x**2




# =============================================================
# 2. DEFINE DIFFERENTIAL EQUATION
# -------------------------------------------------------------
# Schrödinger Equation:
#    ψ''(x) = (2m/ħ²) * [V(x) - E] * ψ(x)
# =============================================================
def d2y_dx2(x, y, g, E):
    mass = 1     # m = 1
    h_cut = 1    # ħ = 1 (natural units)
    return (V(x) - E) * y * 2 * mass / h_cut**2

# =============================================================
# 3. ODE SOLVER (Shooting Integration)
# -------------------------------------------------------------
# Solves the Schrödinger ODE using modified Euler / Heun method
#
# PARAMETERS:
#   initial_state = (xi, yi, gi)
#       xi = starting position
#       yi = ψ(xi)
#       gi = ψ'(xi)
#   boundary_state = xf (final position)
#   E = trial energy
#
# RETURNS:
#   xx, yy_modified, y_boundary
#       xx: grid points
#       yy_modified: wavefunction values
#       y_boundary: final value ψ(xf)
# =============================================================
def sol_ode(initial_state, boundary_state, E):
    n = 5000                   # Change this for resolution
    xf = boundary_state
    xi, yi, gi = initial_state
    h = (xf - xi) / (n - 1)     # Step size

    xx = np.linspace(xi, xf + h, n + 1)
    yy_modified = np.zeros_like(xx)
    gg_modified = np.zeros_like(xx)

    yy_modified[0], gg_modified[0] = yi, gi

    # --- Heun’s (Improved Euler) Integration Loop ---
    for i in range(n):
        gg_temp = gg_modified[i] + h * d2y_dx2(xx[i], yy_modified[i], gg_modified[i], E)
        yy_temp = yy_modified[i] + h * gg_temp

        gg_modified[i + 1] = gg_modified[i] + h / 2 * (
            d2y_dx2(xx[i + 1], yy_temp, gg_temp, E) +
            d2y_dx2(xx[i], yy_modified[i], gg_modified[i], E)
        )
        yy_modified[i + 1] = yy_modified[i] + h / 2 * (gg_modified[i] + gg_temp)

        #gg_modified[i+1] = gg_modified[i] + h * d2y_dx2(xx[i], yy_modified[i], gg_modified[i])
        #yy_modified[i+1] = yy_modified[i] + h * gg_modified[i+1]

    y_boundary = yy_modified[n]
    return xx, yy_modified, y_boundary

# =============================================================
# 4. BOUNDARY CONDITIONS
# -------------------------------------------------------------
# Modify these if your potential has different domain or BCs
# Example:
#   - Infinite well: ψ(-L/2)=ψ(L/2)=0
#   - Harmonic oscillator: ψ(±∞)=0
# =============================================================
xi, xf = -10, 10   # Integration limits
yi, yf = 0, 0     # ψ(xi)=ψ(xf)=0
gg_shoot = 2      # Initial guess for ψ'(xi)


# =============================================================
# 5. SCAN OVER ENERGIES TO FIND EIGENVALUES
# -------------------------------------------------------------
# Adjust range of `Energys` for different systems.
# =============================================================
fig, ax = plt.subplots(figsize=[12, 8])
start_time = time.time()

Energys = np.linspace(0, 4, 5000)
y_finals = [sol_ode((xi, yi, gg_shoot), xf, E)[2] for E in Energys]

end_time = time.time()
print(f"Final Shooting Method Run Time: {end_time - start_time:.4f} seconds")

plt.plot(Energys, y_finals)
plt.xlabel("Energy Eigen Value (E)")
plt.ylabel("ψ(xf)")
plt.title("Shooting Method for Eigenvalue Problem")
plt.grid(True)
plt.show()

# =============================================================
# 6. ROOT FINDING FOR EIGENVALUES (GENERALIZED)
# -------------------------------------------------------------
# For bound states (LHO, wells): detects sign change of ψ(xf)
# For barriers / scattering: detects minima of |ψ(xf)|
# =============================================================
roots = []

# Compute absolute boundary amplitude
abs_yf = np.abs(y_finals)

for i in range(1, len(Energys) - 1):
    # --- Case 1: Bound-state (sign change) ---
    if y_finals[i] * y_finals[i + 1] < 0:
        roots.append((Energys[i] + Energys[i + 1]) / 2)

    # --- Case 2: Quasi-bound / Barrier (local minima) ---
    elif abs_yf[i] < abs_yf[i - 1] and abs_yf[i] < abs_yf[i + 1]:
        roots.append(Energys[i])

# Remove duplicates and round
roots = sorted(list(set(np.round(roots, 3))))
print("Eigen energies ≈", roots)
E_n = np.array(roots)


# =============================================================
# 7. PLOT NORMALIZED WAVEFUNCTION FOR CHOSEN EIGENSTATE
# -------------------------------------------------------------
#  Specify which eigenstate you want to visualize:
#    n_index = 0 → Ground state
#    n_index = 1 → First excited state
#    n_index = 2 → Second excited state, etc.
# =============================================================

n_index = 0  # Change this to plot desired eigenstate

E_selected = E_n[n_index]

fig, ax = plt.subplots(figsize=[12, 8])
xx, yy_modified, y_boundary_i = sol_ode((xi, yi, gg_shoot), xf, E_selected)

# --- Normalize wavefunction ---
norm = np.trapz(yy_modified**2, xx)**0.5
yy_norm = yy_modified / norm

# --- Plot Potential + Wavefunction ---
plt.plot(xx, V(xx), color="red", alpha=0.6, label="Potential  V(x)")
plt.plot(xx, yy_norm**2 + E_selected,
         label=f"ψ²(x) + Eₙ (n = {n_index})")

plt.xlabel("x")
plt.ylabel("Energy / Wavefunction")
plt.title(f"Shooting Method: Eigenstate n = {n_index}")
plt.legend()
plt.grid(True)
plt.show()

# =============================================================
# 8. OPTIONAL: REFINED SHOOTING LOOP (COMMENTED)
# -------------------------------------------------------------
# Use this section to iteratively refine ψ'(0)
# using bisection to minimize ψ(xf) error.
# Uncomment and modify as needed.
# =============================================================

"""
# --- Initial derivative guesses ---
gg_shoot_i = 1
gg_shoot_f = 2

# --- First two trial integrations ---
xx, yy_modified, y_boundary_i = sol_ode((xi, yi, gg_shoot_i), xf, E_n[1])
plt.plot(xx, 2*yy_modified, color="black", alpha=0.6)
xx, yy_modified, y_boundary_f = sol_ode((xi, yi, gg_shoot_f), xf, E_n[1])
plt.plot(xx, yy_modified, color="black", alpha=0.2)

error_i = yf - y_boundary_i
error_f = yf - y_boundary_f
tolerance = 1e-6

# --- Shooting method iteration ---
while abs(error_f - error_i) >= tolerance:
    if error_i * error_f < 0:
        c = (gg_shoot_i + gg_shoot_f) / 2
        xx, yy_modified, y_boundary_c = sol_ode((xi, yi, c), xf, E_n[0])
        plt.plot(xx, yy_modified, color="black", alpha=0.2)
        error_c = yf - y_boundary_c

        if error_c * error_f < 0:
            gg_shoot_i, error_i = c, error_c
        elif error_c * error_i < 0:
            gg_shoot_f, error_f = c, error_c
        else:
            print("Converged or undefined behavior")
            break

# --- Final refined solution ---
xx, yy_modified, _ = sol_ode((xi, yi, c), xf, E_n[0])
plt.plot(xx, yy_modified, color="blue", linewidth=2,
         label=f"Shooting Method (g = {c:.6f})")

plt.xlabel("x")
plt.ylabel("ψ(x)")
plt.title("Refined Shooting Method vs Analytical")
plt.legend()
plt.grid(True)
plt.show()
"""
