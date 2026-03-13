import matplotlib.pyplot as plt
from matplotlib.animation import FuncAnimation

x_data = []
y_data = []

fig, ax = plt.subplots()
line, = ax.plot([], [], marker='o')

ax.set_xlabel("X values (Independent Variable)")
ax.set_ylabel("Y values (Dependent Variable)")
ax.set_title("Live Dynamic X-Y Plot")
ax.grid(True)

def update(frame):
    try:
        x = float(input("Enter X value: "))
        y = float(input("Enter Y value: "))
        
        x_data.append(x)
        y_data.append(y)

        line.set_data(x_data, y_data)
        ax.relim()
        ax.autoscale_view()

    except:
        print("Invalid input")

    return line,

ani = FuncAnimation(fig, update, interval=2000)

plt.show()