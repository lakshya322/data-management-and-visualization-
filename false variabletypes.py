import matplotlib.pyplot as plt

x = [1,2,3,4,5]

y = [10,26,33,47,50]
plt.plot(x,y,marker ='o')

plt.xlabel("X values(independent variale)")
plt.ylabel("Y values(Dependent Variable)")

plt.title("X-Y data plot")

plt.grid(False)

plt.show()