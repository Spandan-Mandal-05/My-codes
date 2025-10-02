import numpy as np
import matplotlib.pyplot as plt

# Generate synthetic data
np.random.seed(42)  # For reproducibility
t = np.linspace(0, 200, 500)  # Time variable
signal = 0.08 * np.exp(-t / 60) * np.sin(2 * np.pi * t / 15) + 0.01 * np.random.randn(len(t))

# Create figure and axis
fig, ax = plt.subplots(figsize=(6, 4), facecolor='black')
ax.set_facecolor('black')
ax.plot(t, signal, color='white', linewidth=1)

# Set labels and limits
ax.set_xlabel('$t$', fontsize=14, color='white')
ax.set_ylabel('$\Delta h_{KS}$', fontsize=14, color='white')
ax.set_xlim(0, 200)
ax.set_ylim(-0.08, 0.1)

# Add text annotation (legend in the plot)
ax.text(150, 0.07, 'K=10\nN=4', fontsize=12, color='white')

# Customize ticks
ax.tick_params(direction='in', length=6, width=1, colors='white')

# Remove grid lines for a cleaner aesthetic
ax.grid(False)

# Show the plot
plt.show()

