import matplotlib.pyplot as plt
import numpy as np
x= list(map(int,input("Enter X values:").split()))
y= list(map(int,input("Enter y values:").split()))

x=np.array(x)
y=np.array(y)

plt.bar(x,y)

plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.title("dynamic bar chart")

plt.show()