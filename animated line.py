import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


fig, ax = plt.subplots()
x = np.linspace(0, 2*np.pi, 400)
line, = ax.plot(x, np.sin(x))

ax.set_ylim(-1.5, 1.5)
ax.set_title("Animated Sine Wave")


def update(frame):
    line.set_ydata(np.sin(x + frame / 10))  
    return line,


ani = FuncAnimation(fig, update, frames=200, interval=30)

plt.show()