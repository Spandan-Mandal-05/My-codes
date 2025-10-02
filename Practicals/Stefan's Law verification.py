import numpy as np
import matplotlib.pyplot as plt

plt.style.use('grayscale')

alpha = 5.21e-3
beta = 7.20e-7
r_draper = 2.18
r = r_draper / 3.9456
voltages = np.arange(1,5.75,0.25) 
current= np.array([304,334,367,397,426,453,479,505,529,552,575,598,619,640,660,680,700,720,738])  
currents= current/1000


def calculate_temperature(V, I):
    R = V / I
    a = beta
    b = alpha
    c = (1 - R/r)
    
    
    discriminant = b**2 - 4*a*c
    
    
    T1 = (-b + np.sqrt(discriminant)) / (2*a)
    T2 = (-b - np.sqrt(discriminant)) / (2*a)
    
    
    return np.where(discriminant > 0, np.where(T1 > 0, T1, T2), np.nan)+273.15



temperatures = calculate_temperature(voltages, currents)
powers = voltages * currents


valid_indices = ~np.isnan(temperatures)
temperatures = temperatures[valid_indices]
powers = powers[valid_indices]


ln_temperatures = np.log(temperatures)
ln_powers = np.log(powers)


slope, intercept = np.polyfit(ln_temperatures, ln_powers, 1)

fit_line = slope * ln_temperatures + intercept


plt.figure(figsize=(8, 6))
plt.scatter(ln_temperatures, ln_powers, label='Data Points')
plt.plot(ln_temperatures, fit_line, 'r-', label=f'Fitted Line: y = {slope:.2f}x + {intercept:.2f}')
plt.xlabel('ln(Temperature)')
plt.ylabel('ln(Power)')
plt.title('Least Squares Fit to ln(T) vs ln(P)')
plt.legend()
plt.grid(True)
plt.show()


print(f"The slope of the fitted line (n) is: {slope:.2f}")