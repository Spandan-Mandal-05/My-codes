# Gauss Dimination Method with Backend Substitution

import numpy as np

A = np.array([
    [20, 5, 5, 13],
    [5, 15, 5, 13],
    [5, 5, 15, 13]
], dtype = float )

print("Initial Matrix :")
print(np.round(A,3))

n = len(A)
for i in range (0,n-1,1):
    g = i + np.argmax(A[i:,i])
    A[[i,g]] = A[[g,i]]

    for j in range(i+1,n,1):
        u = A[j,i]/A[i,i]
        A[j,i:] = A[j,i:] - u * A[i,i:]

print("Gaussian Eleminated Matrix :")
print(np.round(A,2))

xx = np.zeros(n)

for i in range ((n-1),-1,-1):
	s = np.sum(A[i,i+1:n] * xx[i+1:])
	
	xx[i] = ( A[i,n] - s) /A[i,i]
	
print(np.round(xx,3))

