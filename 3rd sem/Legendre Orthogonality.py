import numpy as np

#Legendre polynomial P_n(x)
def P_n(n, x): 
    if n == 0:
        return np.ones_like(x)  # Return an array of ones for P_0
    elif n == 1:
        return x  # Return x for P_1
    else:
        P_n_0 = np.ones_like(x)  # Initialize P_0 as ones
        P_n = x  # Initialize P_1 as x
        for i in range(1, n): 
            #Produce Higher order Legendre Equation using recurrence relation
            P_n_1 = ((2 * i + 1) * x * P_n - i * P_n_0) / (i + 1) 
            P_n_0, P_n = P_n, P_n_1
        return P_n

#calculate the integral of the product of P_i and P_j
def integral(i,j):
    xx = np.linspace(-1,1,10**2+1) # Define x values
    yy = P_n(i,xx)*P_n(j,xx) # Compute the product P_i(x) * P_j(x) for each x
    h = abs(xx[1] - xx[0]) # Calculate step size for Simpson's Rule
    
    # Simpson's Rule to approximate the integral of P_i(x) * P_j(x)
    simpson = h/3 * ( yy[0] + yy[-1] + 4*np.sum(yy[1:-1:2]) + 2*np.sum(yy[2:-2:2]) )
    return simpson

Legendre = np.zeros((10,10))
for i in range (10):
    for j in range (10):
        Legendre[i,j] = round(integral(i,j),3)
# Display the 10x10 matrix to show Orthogonality
print(Legendre)