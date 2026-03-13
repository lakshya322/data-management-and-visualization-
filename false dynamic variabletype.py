import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

# take inputs first
n = int(input("How many points? "))
x = []
y = []

for i in range(n):
    x.append(float(input("Enter X: ")))
    y.append(float(input("Enter Y: ")))

fig, ax = plt.subplots()
line, = ax.plot([], [], 'o-')

ax.set_xlabel("X values")
ax.set_ylabel("Y values")
ax.set_title("Dynamic X-Y Plot")

def update(i):
    line.set_data(x[:i+1], y[:i+1])
    ax.relim()
    ax.autoscale_view()
    return line,

FuncAnimation(fig, update, frames=len(x), interval=800)

plt.show()