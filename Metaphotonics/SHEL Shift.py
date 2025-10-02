import numpy as np
import matplotlib.pyplot as plt 
import pandas as pd 

# Load the Excel file
df = pd.read_excel("C:/Spandan E/Meta Photonics/Amor_Sb2S3.xlsx")

# Load wavelength-based data
wavelengths = df['lambda (nm)'].iloc[0:148].to_numpy()
T_s = df['Transmittance_s'].iloc[0:148].to_numpy() 
R_s = df['Reflectance_s'].iloc[0:148].to_numpy()
T_p = df['Transmittance_p'].iloc[0:148].to_numpy()
R_p = df['Reflectance_p'].iloc[0:148].to_numpy()
argT_s = df['argT_s'].iloc[0:148].to_numpy()
argT_p = df['argT_p'].iloc[0:148].to_numpy()
argR_s = df['argR_s'].iloc[0:148].to_numpy()
argR_p = df['argR_p'].iloc[0:148].to_numpy()
fis_lambda_T = argT_p - argT_s  # Phase difference_p vs wavelength
fis_lambda_R = argR_p - argR_s  # Phase difference_p vs wavelength

# ------------------ SHEL Shift Calculation ------------------
def SHEL_shift(theta, wavelength, fi, mode1 , mode2):
    pi = np.pi
    theta_rad = np.radians(theta)
    if mode1 == "T":
        if mode2 == pi/2:  # V polarization
            return wavelength * (1 - np.sqrt(T_p / T_s) * np.cos(fi)) / (2 * pi * np.tan(theta_rad))
        elif mode2 == 0:   # H polarization
            return wavelength * (1 - np.sqrt(T_s / T_p) * np.cos(fi)) / (2 * pi * np.tan(theta_rad))
    if mode1 == "R":
        if mode2 == pi/2:  # V polarization
            return wavelength * (1 + np.sqrt(R_p / R_s) * np.cos(fi)) / (2 * pi * np.tan(theta_rad))
        elif mode2 == 0:   # H polarization
            return wavelength * (1 + np.sqrt(R_s / R_p) * np.cos(fi)) / (2 * pi * np.tan(theta_rad))

theta_0 = np.radians(5)
# Compute Transmittance-based SHEL shifts
shift_V_T = SHEL_shift(theta_0, wavelengths, fis_lambda_T, "T", np.pi/2)
shift_H_T = SHEL_shift(theta_0, wavelengths, fis_lambda_T, "T", 0)

# Normalize the Transmittance-based shifts by wavelength
norm_shift_H_T = shift_H_T / wavelengths
norm_shift_V_T = shift_V_T / wavelengths

# Compute Reflectance-based SHEL shifts
shift_V_R = SHEL_shift(theta_0, wavelengths, fis_lambda_R, "R", np.pi/2)
shift_H_R = SHEL_shift(theta_0, wavelengths, fis_lambda_R, "R", 0)

# Normalize Reflectance-based shifts by wavelength
norm_shift_H_R = shift_H_R / wavelengths
norm_shift_V_R = shift_V_R / wavelengths

# Plotting
fig, axs = plt.subplots(2, 2, figsize=(9, 8), dpi=120)
axs = axs.flatten()
labels = ['Transmitted H-pol', 'Transmitted V-pol', 'Reflected H-pol', 'Reflected V-pol']
shifts_amor = [shift_H_T, shift_V_T, shift_H_R, shift_V_R]
colors = ['red', 'blue', 'red', 'blue']
linestyles = ['-', '--', '-', '--']

for i in range(4):
    axs[i].plot(wavelengths, shifts_amor[i]/10**6, linestyle=linestyles[i], color=colors[i])
    axs[i].axvline(x=750, color='black', linestyle='--', alpha=0.5)
    axs[i].text(750 + 5, max(shifts_amor[i])*0.1, '750 nm', rotation=90, alpha=0.5)
    axs[i].set_title(labels[i])
    axs[i].set_xlabel('Wavelength (nm)')
    axs[i].set_ylabel('SHEL Shift (mm)')
    axs[i].grid(True)

plt.subplots_adjust(top=0.90, hspace=0.4, wspace=0.3)
fig.suptitle("SHEL Shift vs Wavelength for Different Polarizations", fontsize=14)
plt.show()

df = pd.read_excel("C:/Spandan E/Meta Photonics/Cryst_Sb2S3.xlsx")

T_s = df['Transmittance_s'].iloc[0:148].to_numpy() 
R_s = df['Reflectance_s'].iloc[0:148].to_numpy()
T_p = df['Transmittance_p'].iloc[0:148].to_numpy()
R_p = df['Reflectance_p'].iloc[0:148].to_numpy()
argT_s = df['argT_s'].iloc[0:148].to_numpy()
argT_p = df['argT_p'].iloc[0:148].to_numpy()
argR_s = df['argR_s'].iloc[0:148].to_numpy()
argR_p = df['argR_p'].iloc[0:148].to_numpy()
fis_lambda_T = argT_p - argT_s  # Phase difference_p vs wavelength
fis_lambda_R = argR_p - argR_s  # Phase difference_p vs wavelength

# Compute Transmittance-based SHEL shifts
shift_V_T = SHEL_shift(theta_0, wavelengths, fis_lambda_T, "T", np.pi/2)
shift_H_T = SHEL_shift(theta_0, wavelengths, fis_lambda_T, "T", 0)

# Normalize the Transmittance-based shifts by wavelength
norm_shift_H_T = shift_H_T / wavelengths
norm_shift_V_T = shift_V_T / wavelengths

# Compute Reflectance-based SHEL shifts
shift_V_R = SHEL_shift(theta_0, wavelengths, fis_lambda_R, "R", np.pi/2)
shift_H_R = SHEL_shift(theta_0, wavelengths, fis_lambda_R, "R", 0)

# Normalize Reflectance-based shifts by wavelength
norm_shift_H_R = shift_H_R / wavelengths
norm_shift_V_R = shift_V_R / wavelengths

# Plotting
fig, axs = plt.subplots(2, 2, figsize=(9, 8), dpi=120)
axs = axs.flatten()
labels = ['Transmitted H-pol', 'Transmitted V-pol', 'Reflected H-pol', 'Reflected V-pol']
shifts_cryst = [shift_H_T, shift_V_T, shift_H_R, shift_V_R]
colors = ['red', 'blue', 'red', 'blue']
linestyles = ['-', '--', '-', '--']

for i in range(4):
    axs[i].plot(wavelengths, shifts_cryst[i]/10**6, linestyle=linestyles[i], color=colors[i])
    axs[i].axvline(x=750, color='black', linestyle='--', alpha=0.5)
    axs[i].text(750 + 5, max(shifts_cryst[i])*0.1, '750 nm', rotation=90, alpha=0.5)
    axs[i].set_title(labels[i])
    axs[i].set_xlabel('Wavelength (nm)')
    axs[i].set_ylabel('SHEL Shift (mm)')
    axs[i].grid(True)

plt.subplots_adjust(top=0.90, hspace=0.4, wspace=0.3)
fig.suptitle("SHEL Shift vs Wavelength for Different Polarizations", fontsize=14)
plt.show()


# Plotting
fig, axs = plt.subplots(2, 2, figsize=(9, 8), dpi=120)
axs = axs.flatten()
labels = ['Transmitted H-pol (|Δ amor-cryst|)', 'Transmitted V-pol', 'Reflected H-pol', 'Reflected V-pol']
dif_shifts = [np.abs(c - a) for c, a in zip(shifts_cryst, shifts_amor)]

colors = ['green'] * 4
linestyles = ['-'] * 4

for i in range(4):
    axs[i].plot(
        wavelengths, 
        dif_shifts[i]/1e6, 
        linestyle=linestyles[i], 
        color=colors[i], 
        label = f"max shift at = {np.round(wavelengths[np.argmax(dif_shifts[i])], 2)} nm"
    )
    axs[i].axvline(x=750, color='black', linestyle='--', alpha=0.5)
    axs[i].text(755, np.max(dif_shifts[i])*0.1/1e6, '750 nm', rotation=90, alpha=0.5)
    axs[i].set_title(labels[i])
    axs[i].set_xlabel('Wavelength (nm)')
    axs[i].set_ylabel('Δ SHEL Shift (mm)')
    axs[i].grid(True)
    axs[i].legend(loc='upper right', fontsize=8)

plt.subplots_adjust(top=0.90, hspace=0.4, wspace=0.3)
fig.suptitle("Difference in SHEL Shift: Crystalline vs Amorphous", fontsize=14)
plt.show()

