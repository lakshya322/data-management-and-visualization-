import numpy as np
import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation


fig, ax = plt.subplots()

data = np.random.randn(1000)


n, bins, patches = ax.hist(data, bins=20, color='skyblue', edgecolor='black')

ax.set_xlim(-4, 4)
ax.set_ylim(0, 200)
ax.set_title("Dynamic Histogram")
ax.set_xlabel("Value")
ax.set_ylabel("Frequency")

def update(frame):
    ax.cla()  
    
  
    data = np.random.randn(1000)
    
    
    ax.hist(data, bins=20, color='skyblue', edgecolor='black')
    
    ax.set_xlim(-4, 4)
    ax.set_ylim(0, 200)
    ax.set_title("Dynamic Histogram")
    ax.set_xlabel("Value")
    ax.set_ylabel("Frequency")


ani = FuncAnimation(fig, update, interval=500)

plt.show()