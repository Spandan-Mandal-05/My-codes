import numpy as np

# Augmented matrix [A|b] representing the system of linear equations
A = np.array([
    [1, -1, -1, 0, 0],
    [4, 5, 0, 3, 5],
    [0, 3, -6, 14, 3],
    [4, 0, 7, -6, 5]
])

n = len(A)  # Number of equations (rows)

# Forward Elimination (Gauss Elimination)
for i in range(0, n-1):
    # Partial pivoting: swap row with maximum element in current column
    g = i + np.argmax(A[i:, i])
    A[[i, g]] = A[[g, i]]

    # Eliminate entries below the pivot
    for j in range(i+1, n):
        u = A[j, i] / A[i, i]  # Multiplier for the current row
        A[j, i:] = A[j, i:] - u * A[i, i:]

print("Upper Triangular Matrix:")
print(A)

# Back Substitution to find the solution vector I
I = np.zeros(n)
for k in range(n-1, -1, -1):
    s = np.sum(A[k, k+1:n] * I[k+1:])  # Sum of known variables
    I[k] = (A[k, n] - s) / A[k, k]     # Solve for current variable

# Print the result rounded to 3 decimal places
print("Solution (Currents):")
print(np.round(I, 3))

print("I_0 =", np.round(I[0],3))
print("I_1 =", np.round(I[1],3))
print("I_2 =", np.round(I[2],3))
print("I_3 =", np.round(I[3],3))
