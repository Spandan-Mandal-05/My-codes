import numpy as np
import matplotlib.pyplot as plt 
import pandas as pd 

# Load the Excel file
#df = pd.read_excel("C:/Spandan E/Meta Photonics/Amor_Sb2S3.xlsx")
df = pd.read_excel("C:/Spandan E/Meta Photonics/Cryst_Sb2S3.xlsx")


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

# ------------------ Plot Transmittance vs Wavelength ------------------
plt.figure(figsize=(8, 5))
plt.plot(wavelengths, T_s, color="red", linestyle='-', linewidth=2, label='Tₛ (s-pol)')
plt.plot(wavelengths, T_p, color="blue", linestyle='--', linewidth=2, label='Tₚ (p-pol)')
plt.axvline(x=750, color='black', linestyle='--', linewidth=1.5)  # Visible limit
plt.text(755, 0.5, '750 nm', rotation=90, color='gray', fontsize=9)
plt.xlabel("Wavelength (nm)", fontsize=12)
plt.ylabel("Transmittance", fontsize=12)
plt.title("Transmittance vs Wavelength", fontsize=14, fontweight='bold')
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(fontsize=11)
plt.tight_layout()


# ------------------ Plot Reflectance vs Wavelength ------------------
plt.figure(figsize=(8, 5))
plt.plot(wavelengths, R_s, color="red", linestyle='-', linewidth=2, label='Rₛ (s-pol)')
plt.plot(wavelengths, R_p, color="blue", linestyle='--', linewidth=2, label='Rₚ (p-pol)')
plt.axvline(x=750, color='black', linestyle='--', linewidth=1.5)  # Visible limit
plt.text(755, 0.5, '750 nm', rotation=90, color='gray', fontsize=9)
plt.xlabel("Wavelength (nm)", fontsize=12)
plt.ylabel("Reflectance", fontsize=12)
plt.title("Reflectance vs Wavelength", fontsize=14, fontweight='bold')
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(fontsize=11)
plt.tight_layout()
plt.show()
"""
# ------------------ Plot Phase Difference_T vs Wavelength ------------------
plt.figure(figsize=(8, 5))
plt.plot(wavelengths, abs(fis_lambda_T), color="black", linewidth=2, label='ϕ = arg(tp) – arg(ts)')
plt.axhline(y=np.pi, color='red', linestyle='--', linewidth=1.2, label='+π')
plt.axhline(y=-np.pi, color='blue', linestyle='--', linewidth=1.2, label='–π')
plt.axvline(x=750, color='black', linestyle='--', linewidth=1.5)
plt.xlabel("Wavelength (nm)", fontsize=12)
plt.ylabel("Phase Difference (radians)", fontsize=12)
plt.title("Phase Difference vs Wavelength", fontsize=14, fontweight='bold')
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(fontsize=11)
plt.tight_layout()


# ------------------ Plot Phase Difference_R vs Wavelength ------------------
plt.figure(figsize=(8, 5))
plt.plot(wavelengths, abs(fis_lambda_R), color="black", linewidth=2, label='ϕ = arg(rp) – arg(rs)')
plt.axhline(y=np.pi, color='red', linestyle='--', linewidth=1.2, label='+π')
plt.axhline(y=-np.pi, color='blue', linestyle='--', linewidth=1.2, label='–π')
plt.axvline(x=750, color='black', linestyle='--', linewidth=1.5)
plt.xlabel("Wavelength (nm)", fontsize=12)
plt.ylabel("Phase Difference (radians)", fontsize=12)
plt.title("Reflectance Phase Difference vs Wavelength", fontsize=14, fontweight='bold')
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(fontsize=11)
plt.tight_layout()
plt.show()
"""
# Load angle-based data
theta_i = df['theta_i'].iloc[0:101].to_numpy()
T_s_deg = df['Transmittance_s_deg'].iloc[0:101].to_numpy() 
T_p_deg = df['Transmittance_p_deg'].iloc[0:101].to_numpy()
argT_s_deg = df['argT_s_deg'].iloc[0:101].to_numpy()
argT_p_deg = df['argT_p_deg'].iloc[0:101].to_numpy()
fis_deg_T = argT_p_deg - argT_s_deg
R_s_deg = df['Reflectance_s_deg'].iloc[0:101].to_numpy() 
R_p_deg = df['Reflectance_p_deg'].iloc[0:101].to_numpy()
argR_s_deg = df['argR_s_deg'].iloc[0:101].to_numpy()
argR_p_deg = df['argR_p_deg'].iloc[0:101].to_numpy()
fis_deg_R = argR_p_deg - argR_s_deg
"""
# ------------------ Plot Transmittance Phase Difference vs Angle ------------------
plt.figure(figsize=(8, 5))
plt.plot(theta_i, abs(fis_deg_T), color="black", linewidth=2, label='ϕ = arg(tp) – arg(ts)')
plt.axhline(y=np.pi, color='red', linestyle='--', linewidth=1.2, label='+π')
plt.axhline(y=-np.pi, color='blue', linestyle='--', linewidth=1.2, label='–π')
plt.xlabel("Incident Angle θᵢ (deg)", fontsize=12)
plt.ylabel("Phase Difference (radians)", fontsize=12)
plt.title("Transmittance Phase Difference vs Incident Angle", fontsize=14, fontweight='bold')
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(fontsize=11)
plt.tight_layout()
plt.show()
"""
# ------------------ SHEL Shift Calculation ------------------
def SHEL_shift(theta, wavelength, fi, mode1 , mode2):
    pi = np.pi
    theta_rad = np.radians(theta)
    if mode1 == "T":
        if mode2 == pi/2:  # V polarization
            return wavelength * (1 - np.sqrt(T_p_deg / T_s_deg) * np.cos(fi)) / (2 * pi * np.tan(theta_rad))
        elif mode2 == 0:   # H polarization
            return wavelength * (1 - np.sqrt(T_s_deg / T_p_deg) * np.cos(fi)) / (2 * pi * np.tan(theta_rad))
    if mode1 == "R":
        if mode2 == pi/2:  # V polarization
            return wavelength * (1 + np.sqrt(R_p_deg / R_s_deg) * np.cos(fi)) / (2 * pi * np.tan(theta_rad))
        elif mode2 == 0:   # H polarization
            return wavelength * (1 + np.sqrt(R_s_deg / R_p_deg) * np.cos(fi)) / (2 * pi * np.tan(theta_rad))
        
wavelength = 380  # nm

# Compute Transmittance-based SHEL shifts
shift_V_T = SHEL_shift(theta_i, wavelength, fis_deg_T, "T", np.pi/2)
shift_H_T = SHEL_shift(theta_i, wavelength, fis_deg_T, "T", 0)

# Normalize the Transmittance-based shifts by wavelength
norm_shift_H_T = shift_H_T / wavelength
norm_shift_V_T = shift_V_T / wavelength

# ------------------ Plot Normalized SHEL Shifts (T,H-pol) ------------------
plt.figure(figsize=(8, 5))
plt.plot(theta_i, norm_shift_H_T, 'r-', label='δᴴ / λ (H polarization)')
plt.xlabel("Incident Angle θᵢ (degrees)", fontsize=12)
plt.ylabel("Normalized SHEL Shift (δᴴ / λ)", fontsize=12)
plt.title("Normalized Transmittance SHEL Shift vs Incident Angle (H-pol)", fontsize=14, fontweight='bold')
plt.grid(True, linestyle='--', alpha=0.6)
plt.axhline(y=1, linestyle='-.', color='Black', label='1λ')
plt.legend()
plt.tight_layout()


# ------------------ Plot Normalized SHEL Shifts (T,V-pol) ------------------
plt.figure(figsize=(8, 5))
plt.plot(theta_i, norm_shift_V_T, 'b--', label='δⱽ / λ (V polarization)')
plt.xlabel("Incident Angle θᵢ (degrees)", fontsize=12)
plt.ylabel("Normalized SHEL Shift (δⱽ / λ)", fontsize=12)
plt.title("Normalized Transmittance SHEL Shift vs Incident Angle (V-pol)", fontsize=14, fontweight='bold')
plt.grid(True, linestyle='--', alpha=0.6)
plt.axhline(y=1,linestyle='-.', color='Black', label='1λ')
plt.legend()
plt.tight_layout()


# ------------------ Plot Efficiencies vs Incident Angle ------------------
plt.figure(figsize=(8, 5))
plt.plot(theta_i, T_p_deg, 'r-', label='Efficiency (H polarization)')
plt.xlabel("Incident Angle θᵢ (degrees)", fontsize=12)
plt.ylabel("Efficiency Tₚ", fontsize=12)
plt.title("Efficiency vs Incident Angle (H-pol)", fontsize=14, fontweight='bold')
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.tight_layout()


plt.figure(figsize=(8, 5))
plt.plot(theta_i, T_s_deg, 'b--', label='Efficiency (V polarization)')
plt.xlabel("Incident Angle θᵢ (degrees)", fontsize=12)
plt.ylabel("Efficiency Tₛ", fontsize=12)
plt.title("Efficiency vs Incident Angle (V-pol)", fontsize=14, fontweight='bold')
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.tight_layout()
plt.show()

"""
# ------------------ Plot Reflectance Phase Difference vs Angle ------------------
plt.figure(figsize=(8, 5))
plt.plot(theta_i, fis_deg_R, color="black", linewidth=2, label='ϕ = arg(rp) – arg(rs)')
plt.axhline(y=np.pi, color='red', linestyle='--', linewidth=1.2, label='+π')
plt.axhline(y=-np.pi, color='blue', linestyle='--', linewidth=1.2, label='–π')
plt.xlabel("Incident Angle θᵢ (deg)", fontsize=12)
plt.ylabel("Phase Difference (radians)", fontsize=12)
plt.title("Reflectance Phase Difference vs Incident Angle", fontsize=14, fontweight='bold')
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend(fontsize=11)
plt.tight_layout()
#plt.show()
"""
# Compute Reflectance-based SHEL shifts
shift_V_R = SHEL_shift(theta_i, wavelength, fis_deg_R, "R", np.pi/2)
shift_H_R = SHEL_shift(theta_i, wavelength, fis_deg_R, "R", 0)

# Normalize Reflectance-based shifts by wavelength
norm_shift_H_R = shift_H_R / wavelength
norm_shift_V_R = shift_V_R / wavelength

# ------------------ Plot Normalized SHEL Shift (R, H-pol) ------------------
plt.figure(figsize=(8, 5))
plt.plot(theta_i, norm_shift_H_R, 'r-', label='δᴴ / λ (H polarization)')
plt.xlabel("Incident Angle θᵢ (degrees)", fontsize=12)
plt.ylabel("Normalized SHEL Shift (δᴴ / λ)", fontsize=12)
plt.title("Reflectance SHEL Shift vs Incident Angle (H-pol)", fontsize=14, fontweight='bold')
plt.grid(True, linestyle='--', alpha=0.6)
plt.axhline(y=1, linestyle='-.', color='Black', label='1λ')
plt.legend()
plt.tight_layout()

# ------------------ Plot Normalized SHEL Shift (R, V-pol) ------------------
plt.figure(figsize=(8, 5))
plt.plot(theta_i, norm_shift_V_R, 'b--', label='δⱽ / λ (V polarization)')
plt.xlabel("Incident Angle θᵢ (degrees)", fontsize=12)
plt.ylabel("Normalized SHEL Shift (δⱽ / λ)", fontsize=12)
plt.title("Reflectance SHEL Shift vs Incident Angle (V-pol)", fontsize=14, fontweight='bold')
plt.grid(True, linestyle='--', alpha=0.6)
plt.axhline(y=1,linestyle='-.', color='Black', label='1λ')
plt.legend()
plt.tight_layout()


# ------------------ Reflectance Efficiency vs Angle (H-pol) ------------------
plt.figure(figsize=(8, 5))
plt.plot(theta_i, R_p_deg, 'r-', label='Efficiency (H polarization)')
plt.xlabel("Incident Angle θᵢ (degrees)", fontsize=12)
plt.ylabel("Efficiency Rₚ", fontsize=12)
plt.title("Reflectance Efficiency vs Incident Angle (H-pol)", fontsize=14, fontweight='bold')
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.tight_layout()


# ------------------ Reflectance Efficiency vs Angle (V-pol) ------------------
plt.figure(figsize=(8, 5))
plt.plot(theta_i, R_s_deg, 'b--', label='Efficiency (V polarization)')
plt.xlabel("Incident Angle θᵢ (degrees)", fontsize=12)
plt.ylabel("Efficiency Rₛ", fontsize=12)
plt.title("Reflectance Efficiency vs Incident Angle (V-pol)", fontsize=14, fontweight='bold')
plt.grid(True, linestyle='--', alpha=0.6)
plt.legend()
plt.tight_layout()
plt.show()
