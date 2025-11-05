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
from scipy.integrate import solve_ivp  

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
    #V0 = 5.0   # Depth of the well
    #L = 2.0    # Width of the well
    #return np.where(np.abs(x) <= L/2, -V0, 0.0)

    # --- Finite Barrier (Rectangular Barrier) ---
    #V0 = 5.0   # Height of the barrier
    #L = 1.0    # Width of the barrier
    #return np.where(np.abs(x) <= L/2, V0, 0.0)
    #return np.where((x >= 0) & (x <= L), -V0, 0.0)

    # --- Harmonic Oscillator (default) ---
    w = 1  # Frequency ω
    return 0.5 * w**2 * x**2




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
    xi, yi, gi = initial_state
    xf = boundary_state

    # Schrödinger system: y' = g, g' = (2m/ħ²)(V(x) - E)y
    def sch_eq(x, Y):
        y, g = Y
        return [g, 2 * (V(x) - E) * y]   # m = ħ = 1 in natural units

    # Integrate using SciPy’s adaptive RK45 solver
    sol = solve_ivp(
        sch_eq,
        t_span=(xi, xf),
        y0=[yi, gi],
        method='RK45',
        t_eval=np.linspace(xi, xf, 10000),
        rtol=1e-8,
        atol=1e-8
    )

    xx = sol.t
    yy_modified = sol.y[0]
    y_boundary = yy_modified[-1]
    return xx, yy_modified, y_boundary


# =============================================================
# 4. BOUNDARY CONDITIONS
# -------------------------------------------------------------
# Modify these if your potential has different domain or BCs
# Example:
#   - Infinite well: ψ(-L/2)=ψ(L/2)=0
#   - Harmonic oscillator: ψ(±∞)=0
# =============================================================
xi, xf = -4, 4   # Integration limits
yi, yf = 0, 0     # ψ(xi)=ψ(xf)=0
gg_shoot = 2      # Initial guess for ψ'(xi)


# =============================================================
# 5. SCAN OVER ENERGIES TO FIND EIGENVALUES
# -------------------------------------------------------------
# Adjust range of `Energys` for different systems.
# =============================================================
fig, ax = plt.subplots(figsize=[12, 8])
start_time = time.time()

Energys = np.linspace(-5, 2, 1000)
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
roots = sorted(list(set(np.round(roots, 1))))
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
