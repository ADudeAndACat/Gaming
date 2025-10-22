import numpy as np
import matplotlib.pyplot as plt
import matplotlib.animation as animation

# Parameters
sphere_radius = 1.0
shutter_angle = np.pi  # Half sphere, 180 degrees
rotation_speed = np.pi / 24  # radians per time unit (simulate 24 steps = full day)

# Set up figure
fig, ax = plt.subplots(figsize=(6, 6))
ax.set_aspect('equal')
ax.set_xlim(-1.2, 1.2)
ax.set_ylim(-1.2, 1.2)
ax.axis('off')

# Draw Dyson Sphere inner surface
theta = np.linspace(0, 2 * np.pi, 500)
x = sphere_radius * np.cos(theta)
y = sphere_radius * np.sin(theta)
sphere_line, = ax.plot(x, y, color='gray')

# Draw light source (Sun/Core)
core = plt.Circle((0, 0), 0.05, color='yellow', zorder=5)
ax.add_artist(core)

# Initialize shutter (half-circle mask)
shutter_patch = plt.Polygon(np.empty((0, 2)), closed=True, color='black', alpha=0.5)
ax.add_patch(shutter_patch)

# Function to update the animation
def update(frame):
    angle_offset = rotation_speed * frame
    start_angle = angle_offset
    end_angle = angle_offset + shutter_angle

    # Create shutter wedge (shadow area)
    angles = np.linspace(start_angle, end_angle, 100)
    xs = [0] + list(np.cos(angles)) + [0]
    ys = [0] + list(np.sin(angles)) + [0]
    shutter_patch.set_xy(np.column_stack((xs, ys)))
    return shutter_patch,

# Animate
ani = animation.FuncAnimation(
    fig, update, frames=48, interval=200, blit=True
)

# Save animation as GIF
ani.save('dyson_sphere.gif', writer='pillow', fps=5)

# plt.show()  # Disabled for non-interactive environments
