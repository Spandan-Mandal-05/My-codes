import matplotlib.pyplot as plt
import numpy as np
pi=np.pi 
time_sqr=[0.578,0.734,0.856,0.951,1.104]
loads=np.arange(0.05,0.3,0.05)
slope1, intercept1 = np.polyfit(loads,time_sqr, 1)
K=4*pi**2/slope1
print("spring const.",K,"N/m")
extension=np.array([3,5.9,8.9,12,15])/100
slope2, intercept2 = np.polyfit(loads,extension, 1)
g = acc_gra = K * slope2 
print("gravitational acc",g,"m/s^2")

# Generate fit data
fit_loads = np.linspace(-0.050, 0.300, 100)
fit_dif_sq_times = intercept1 + slope1 * fit_loads
fit_extensions = intercept2 + slope2 * fit_loads

# Plot T² vs Load
plt.figure(figsize=(12, 8))
plt.plot(fit_loads, fit_dif_sq_times, label=f"Spring Constant K = {K:.2f} N/m")
plt.scatter(loads, time_sqr, label="Data Points", color='r')
plt.axvline(x=0, alpha=0.6, linestyle="--")
plt.axhline(y=0, alpha=0.6, linestyle="--")
plt.xlabel('Load (gm)')
plt.ylabel('T² (s²)')
plt.title('T² vs Load')
plt.legend()
plt.grid(True)
#plt.show()

# Plot Extension vs Load
plt.figure(figsize=(12, 8))
plt.plot(fit_loads, fit_extensions, label=f"Gravitational Acc. g = {g:.2f} m/s²")
plt.scatter(loads, extension, label="Data Points", color='g')
plt.axvline(x=0, alpha=0.6, linestyle="--")
plt.axhline(y=0, alpha=0.6, linestyle="--")
plt.xlabel('Load (gm)')
plt.ylabel('Extension (cm)')
plt.title('Load vs Extension')
plt.legend()
plt.grid(True)
#plt.show()

# Compute constants
R = 1.14075/100
r = 0.0593 / 100
N = 108
G = rigidity_modulus = K*4*N*R**3/r**4
print(f"Rigidity Modulus = {G/10**9}")
