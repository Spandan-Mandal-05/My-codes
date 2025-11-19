# =============================================================
#  RADIAL SCHRÖDINGER EQUATION (Spherical Symmetry)
#  Author: Spandy
#  Description:
#     Computes eigenenergies and radial wavefunctions u(r)
#     for a spherically symmetric potential using finite difference.
# =============================================================

import numpy as np
import matplotlib.pyplot as plt
from scipy.sparse.linalg import eigsh
import scipy.sparse as sp
import time

# =============================================================
# 1. DEFINE POTENTIAL FUNCTION V(r)
# =============================================================
def V(r):
    # --- Choose ONE potential below ---

    # --- Finite Spherical Well ---
    # V0, R0 = 5.0, 2.0
    # return np.where(r <= R0, -V0, 0.0)

    # --- Finite Barrier ---
    V0, L = 2.0, 1.0
    return np.where((r >= 0) & (r <= L), V0, 0.0)

    # --- Harmonic Oscillator ---
    # w = 1.0
    # return 0.5 * w**2 * r**2

    # --- Coulomb Potential (Hydrogen-like) ---
    # return -1.0 / r


# =============================================================
# 2. SETUP GRID AND CONSTANTS
# =============================================================
ħ = 1.0
m = 1.0
ℓ = 1            # Angular momentum quantum number (0 = s, 1 = p, 2 = d, ...)
r_min, r_max = 1e-4, 10
N = 10000
r = np.linspace(r_min, r_max, N)
h = r[1] - r[0]

# =============================================================
# 3. BUILD EFFECTIVE POTENTIAL (INCLUDES CENTRIFUGAL TERM)
# =============================================================
V_eff = V(r) + (ħ**2 * ℓ * (ℓ + 1)) / (2 * m * r**2)

# =============================================================
# 4. BUILD HAMILTONIAN MATRIX (FINITE DIFFERENCE)
# =============================================================
pref = -ħ**2 / (2 * m * h**2)
main_diag = np.full(N, -2 * pref) + V_eff
off_diag = np.full(N - 1, pref)

start_time = time.time()
H = sp.diags([off_diag, main_diag, off_diag], offsets=[-1, 0, 1], format="csr")

# =============================================================
# 5. SOLVE EIGENVALUE PROBLEM (Sparse Solver)
# =============================================================
num_states = 10
E, u = eigsh(H, k=num_states, sigma=0, which="LM", maxiter=500)
idx = np.argsort(E)
E, u = E[idx], u[:, idx]
end_time = time.time()

# =============================================================
# 6. NORMALIZE WAVEFUNCTIONS (u(r))
# =============================================================
u /= np.sqrt(np.trapz(u**2, r, axis=0))  # normalize each eigenfunction

# =============================================================
# 7. COMPUTE R(r) = u(r)/r (physical radial wavefunction)
# =============================================================
R = u / r[:, np.newaxis]

# =============================================================
# 8. PLOT RESULTS
# =============================================================
plt.figure(figsize=(9,6))
plt.plot(r, V_eff, "r", label="V_eff(r) = V(r) + ℓ(ℓ+1)ħ²/(2mr²)")

for i in range(num_states):
    plt.plot(r, R[:, i]**2 + E[i], label=f"n={i}, E={E[i]:.3f}")

plt.title(f"Radial Schrödinger Equation (ℓ = {ℓ})")
plt.xlabel("r")
plt.ylabel("Energy / |R(r)|²")
plt.legend()
plt.grid(True)
plt.show()

print("Eigenenergies (first few):")
print(E[:num_states])
print(f"Total Run Time: {end_time - start_time:.4f} seconds")
