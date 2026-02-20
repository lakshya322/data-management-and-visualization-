import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


fig, ax = plt.subplots()


radius = 1
theta = np.linspace(0, 2*np.pi, 100)

x_center = 0
y_center = 0


circle_line, = ax.plot([], [])

ax.set_xlim(-5, 5)
ax.set_ylim(-5, 5)
ax.set_aspect('equal')
ax.set_title("Animated Moving Circle")

def update(frame):
   
    x_center = 2 * np.cos(frame / 20)
    y_center = 2 * np.sin(frame / 20)

    x = x_center + radius * np.cos(theta)
    y = y_center + radius * np.sin(theta)

    circle_line.set_data(x, y)
    return circle_line,

ani = FuncAnimation(fig, update, frames=360, interval=30)

plt.show()