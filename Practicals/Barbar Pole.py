import numpy as np
import matplotlib.pyplot as plt
from matplotlib import animation 
from matplotlib.patches import FancyArrow

# Constants
arrow_length = 5
rotation_speed = 2 * np.pi / 100
speed_ratio=4  # Full rotation in 100 frames
a=0
# Set up the figure and axes
fig, ax = plt.subplots()

# Create the arrow
arrow = FancyArrow(0, 0, arrow_length, 0, width=0.1, color='k')
ax.add_patch(arrow)

# Animation function
def animate(frame):
    plt.cla()  # Clear the old arrows
    ax.set_xlim(-10, 10)  # Reset the x-axis limits
    ax.set_ylim(-10, 10)
    ax.set_aspect('equal')
    ax.grid(alpha=0.5)

    # Calculate the rotation angle
    angle = rotation_speed * frame

    # Position for the first arrow
    dx = arrow_length * np.cos(-angle)
    dy = arrow_length * np.sin(-angle)
    arrow = FancyArrow(0, 0, dx, dy, width=0.1, color='k', label='Clockwise Circular Polarization')
    ax.add_patch(arrow)
    
    angleB= angle + np.pi*a
    # Position for the second arrow, which should rotate around the tip of the first arrow
    d_x = arrow_length * np.cos(angleB)  # Double the angle for a different rotation speed
    d_y = arrow_length * np.sin(angleB)
    arrowB = FancyArrow(dx, dy, d_x, d_y, width=0.1, color='r',label='Anti-clockwise Circular Polarization')  # Use a different color for visibility
    ax.add_patch(arrowB)

    arrowR = FancyArrow(0,0, d_x+dx, d_y+dy, width=0.1, color='blue', label= 'Resultant Linear Polarization')  # Use a different color for visibility
    ax.add_patch(arrowR)

    ax.legend()
# Create the animation
ani = animation.FuncAnimation(fig, animate, frames=np.arange(0, 100), interval=50)

# Display the animation
plt.show()