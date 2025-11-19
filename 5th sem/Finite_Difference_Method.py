import numpy as np 
import matplotlib.pyplot as plt 
from scipy.linalg import  solve_banded
# =============================================================
# FINITE DIFFERENCE METHOD FOR 2ND ORDER ODEs

def p(x): return np.exp(x)  #Coefficient of y'
def q(x): return 1*np.ones_like(x) #Coefficient of y
def r(x): return 2*(x-1)*np.exp(-x) -x +1  #Right hand side function
def f(x): return x*np.exp(-x)  #Function for boundary conditions

# =============================================================
# USER INPUT SECTION
# =============================================================

xi = eval(input("Enter left boundary xi: "))
xf = eval(input("Enter right boundary xf: "))
yi = eval(input("Enter boundary value y(xi): "))
yf = eval(input("Enter boundary value y(xf): "))
N  = int(input("Enter number of grid points N: "))

# =============================================================
# 1. DEFINE GRID AND STEP SIZE
# -------------------------------------------------------------
xx = np.linspace(xi, xf, N)  #Grid points
n = len(xx)                 #Number of grid points
h = xx[1] - xx[0]           #Step size
yy_exact = f(xx)          #Exact solution values
pp, qq, rr = p(xx), q(xx), r(xx)
yy = np.zeros_like(xx)  #Initialize solution array
yy[0], yy[-1] = yi, yf  #Boundary conditions
# =============================================================
# 2. CONSTRUCT COEFFICIENT MATRIX A AND RIGHT HAND SIDE VECTOR B
# -------------------------------------------------------------
m = n - 2             #Internal Points
#A = np.zeros((m, m))  #Coefficient matrix
B = np.zeros(m)       #Right hand side vector   
cc = (1 + h*pp/2)           # upper diagonal
dd = (qq*h**2 - 2)          # main diagonal
ee = (1 - h*pp/2)           # lower diagonal
ff = (rr*h**2)              # RHS (zero here)

main = dd[1:-1]
lower = ee[2:-1]
upper = cc[1:-2]
rhs = ff[1:-1]

rhs[0] -= ee[1]*yy[0]
rhs[-1] -= cc[-2]*yy[-1]
B = rhs 

A = np.zeros((m,m))
np.fill_diagonal(A, main)
np.fill_diagonal(A[1:], lower)
np.fill_diagonal(A[:,1:], upper)

yy_internal = np.linalg.solve(A,B)

"""ab = np.zeros((3,m))
ab[0,1:] = upper
ab[1,:] = main
ab[2,:-1] = lower

yy_internal = solve_banded((1,1), ab, B)"""
yy[1:-1] = yy_internal

plt.figure(figsize=(8,5))

plt.plot(xx, yy_exact, 'r--', linewidth=1.8, label="Exact")
plt.plot(xx, yy, 'k', linewidth=1.8, label="Finite Difference")

plt.xlabel("x", fontsize=13)
plt.ylabel("y(x)", fontsize=13)
plt.title("Finite Difference vs Exact Solution", fontsize=14)

plt.grid(True, alpha=0.4)
plt.legend(fontsize=12)

plt.tight_layout()
plt.show()
