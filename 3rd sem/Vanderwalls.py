import matplotlib.pyplot as plt 
import numpy as np

def vanderwaals(V, T):
    P = R * T / (V - b) - a / V**2
    return P 

R = 8.314  # Gas constant in J/(mol·K)

# Parameters for Nitrogen (N₂)
a = 1.39  # Pa·m^6/mol^2
b = 0.0391  # m^3/mol

# Critical constants
Tc = 8 * a / (27 * b * R)
Vc = 3 * b
Pc = a / (27 * b**2)

# Define Volume and Temperature ranges
Volume = np.arange(b + 0.001, 0.1, 0.00001)  # Volume from slightly above b to 3 m^3/mol
Temperature = np.arange(Tc - 0.1, Tc + 0.2, 0.02)  # Close intervals around Tc

# Plot isotherms for different temperatures
for T in Temperature:
    Pressure = vanderwaals(Volume, T)
    if np.all(Pressure > 0):  # Filter out negative pressures (for realistic visualization)
        if T == Tc:
            plt.plot(Volume, Pressure, label=f"Tc = {T:.2f} K", color="black", linewidth=2)
        else:
            plt.plot(Volume, Pressure, linewidth=0.5)

# Display critical temperature, volume, and pressure
print(f"Critical Temperature (Tc): {Tc:.2f} K")
print(f"Critical Volume (Vc): {Vc:.2f} m^3/mol")
print(f"Critical Pressure (Pc): {Pc:.2f} Pa")

# Plot settings
plt.axvline(x=b, color='black', linestyle='--', label="b")  # Mark the excluded volume b
plt.axhline(y=0, color='black', alpha=0.45)
plt.xlabel("Volume (m^3/mol)")
plt.ylabel("Pressure (Pa)")
plt.legend(loc='best')
plt.title("Van der Waals Isotherms for Nitrogen (N₂)")
plt.show()



