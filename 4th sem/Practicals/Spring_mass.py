import numpy as np
import pandas as pd 
import matplotlib.pyplot as plt  

df = pd.read_excel("C:/Spandan E/crome Downloads/Spring Mass System.xlsx")
loads = df['Load (gm)'].to_numpy()
times = df['Mean Time t (sec)'].to_numpy()
extensions = df['Extension L (cm)'].to_numpy()

loads = loads[~pd.isna(loads)]
times = times[~pd.isna(times)]
extensions = extensions[~pd.isna(extensions)]

# Compute squared times
square_times = times ** 2

# Compute differences
dif_loads = loads - loads[0]
dif_square_times = square_times #- square_times[0]

# Perform linear fits
slope1, intercept1 = np.polyfit(dif_loads, dif_square_times, 1)
slope2, intercept2 = np.polyfit(dif_loads, extensions, 1)

# Generate fit data
fit_loads = np.linspace(-50, 300, 100)
fit_dif_sq_times = intercept1 + slope1 * fit_loads
fit_extensions = intercept2 + slope2 * fit_loads

# Compute constants
#R = 
#r = 
#N = 
K = spring_const = 4*np.pi**2/slope1 
g = acc_gra = K * slope2 
#G = rigidity_modulus = K*4*N*R**3/r**4

# Plot T² vs Load
plt.figure(figsize=(12, 8))
plt.plot(fit_loads, fit_dif_sq_times, label=f"Spring Constant K = {K:.2f} N/m")
plt.scatter(dif_loads, dif_square_times, label="Data Points", color='r')
plt.axvline(x=0, alpha=0.6, linestyle="--")
plt.axhline(y=0, alpha=0.6, linestyle="--")
plt.xlabel('Load (gm)')
plt.ylabel('T² (s²)')
plt.title('T² vs Load')
plt.legend()
plt.grid(True)
plt.show()

# Plot Extension vs Load
plt.figure(figsize=(12, 8))
plt.plot(fit_loads, fit_extensions, label=f"Gravitational Acc. g = {g:.2f} m/s²")
plt.scatter(dif_loads, extensions, label="Data Points", color='g')
plt.axvline(x=0, alpha=0.6, linestyle="--")
plt.axhline(y=0, alpha=0.6, linestyle="--")
plt.xlabel('Load (gm)')
plt.ylabel('Extension (cm)')
plt.title('Load vs Extension')
plt.legend()
plt.grid(True)
plt.show()

# Print values
print(f"Spring Constant K = {K:.2f} N/m")
print(f"Gravitational Acceleration g = {g:.2f} m/s²")
#print(f"Rigidity Modulus = {G}")
