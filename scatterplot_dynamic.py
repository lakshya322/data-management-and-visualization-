import matplotlib.pyplot as plt
import numpy as np
x= list(map(int,input("Enter X values:").split()))
y= list(map(int,input("Enter y values:").split()))

plt.scatter(x,y)

plt.xlabel("X Axis")
plt.ylabel("Y Axis")
plt.title("static scatter plot")
plt.show()