import matplotlib.pyplot as plt
from matplotlib.patches import Circle
from matplotlib.animation import FuncAnimation
import random


x, y = 0.5, 0.5
radius = 0.1
color = 'blue'
speed = 0.02


fig, ax = plt.subplots()
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)

circle = Circle((x, y), radius, color=color)
ax.add_patch(circle)

def on_key(event):
    global x, y, radius, color
    
    if event.key == 'left':
        x -= speed
    elif event.key == 'right':
        x += speed
    elif event.key == 'up':
        y += speed
    elif event.key == 'down':
        y -= speed
    elif event.key == '+':
        radius += 0.02
    elif event.key == '-':
        radius = max(0.02, radius - 0.02)
    elif event.key == 'c':
        color = (random.random(), random.random(), random.random())
        circle.set_color(color)


fig.canvas.mpl_connect('key_press_event', on_key)


def update(frame):
    circle.center = (x, y)
    circle.radius = radius
    return circle,

ani = FuncAnimation(fig, update, frames=200, interval=30)

plt.gca().set_aspect('equal', adjustable='box')
plt.title("Interactive Animated Circle (Use Arrow Keys)")
plt.show()