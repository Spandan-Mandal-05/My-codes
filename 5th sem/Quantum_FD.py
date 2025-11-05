# =============================================================
#  FINITE DIFFERENCE METHOD FOR 1D SCHRÖDINGER EQUATION
#  Author: Spandy
#  Description:
#     Finds eigenenergies and wavefunctions for 1D systems
#     using matrix (finite difference) approach.
# =============================================================

import numpy as np
import matplotlib.pyplot as plt
from scipy.sparse.linalg import eigsh
import scipy.sparse as sp
import time
# =============================================================
# 1. DEFINE POTENTIAL FUNCTION V(x)
# =============================================================
def V(x):
    # --- Choose ONE potential below ---
    
    # --- Finite Square Well ---
    #V0, L = 5.0, 2.0
    #return np.where(np.abs(x) <= L/2, -V0, 0.0)

    # --- Infinite Square Well ---
    #L = 2.0
    #return np.where((x >= -L/2) & (x <= L/2), 0.0, 1e6)

    # --- Finite Barrier ---
    V0, L = 2.0, 1.0
    return np.where((x >= 0) & (x <= L), V0, 0.0)

    # --- Harmonic Oscillator ---
    #w = 1.0
    #return 0.5 * w**2 * x**2


# =============================================================
# 2. SETUP GRID AND CONSTANTS
# =============================================================
ħ = 1.0
m = 1.0
x_min, x_max = -5, 5
N = 10**4
x = np.linspace(x_min, x_max, N)
h = x[1] - x[0]

# =============================================================
# 3. BUILD HAMILTONIAN MATRIX
# =============================================================
Vx = V(x)
pref = -ħ**2 / (2 * m * h**2)
main_diag = np.full(N, -2*pref) + Vx
off_diag  = np.full(N-1, pref)

start_time = time.time()
# Use sparse diagonal structure
H = sp.diags([off_diag, main_diag, off_diag], offsets=[-1, 0, 1], format='csr')

# =============================================================
# 4. SOLVE EIGENVALUE PROBLEM (using sparse solver)
# =============================================================

num_states = 10   # number of lowest eigenstates you want
E, psi = eigsh(H, k=num_states, sigma= 0, which='LM', maxiter=500)


# Sort results (sometimes not in order)
idx = np.argsort(E)
E, psi = E[idx], psi[:, idx]
end_time = time.time()
# =============================================================
# 5. PLOT FIRST FEW EIGENSTATES
# =============================================================
plt.figure(figsize=(9,6))
#V_scaled = (Vx - np.min(Vx)) / np.max(Vx - np.min(Vx)) * (E[num_states]*0.5)
#plt.plot(x, V_scaled, 'r', label='Potential (scaled)')
plt.plot(x, Vx, 'r', label='Potential (original)')

for i in range(num_states):
    psi_x = psi[:, i]
    psi_x /= np.trapz(psi_x**2, x)**0.5
    plt.plot(x, psi_x**2 + E[i], label=f'n={i}, E={E[i]:.3f}')

plt.title("Finite Difference Method: 1D Schrödinger Equation")
plt.xlabel("x")
plt.ylabel("Energy / ψ²(x)")
plt.legend()
plt.grid(True)
plt.show()

print("Eigenenergies (first few):")
print(E[:num_states])
print(f"Total Run Time: {end_time - start_time:.4f} seconds")
