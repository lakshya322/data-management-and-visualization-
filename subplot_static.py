import matplotlib.pyplot as plt

# Data
x = [1, 2, 3, 4, 5]
y1 = [10, 20, 15, 25, 30]
y2 = [5, 15, 10, 20, 25]

plt.figure(figsize=(8, 6))

#  Line Chart
plt.subplot(2, 2, 1)
plt.plot(x, y1)
plt.title("Line Chart")

# Bar Chart
plt.subplot(2, 2, 2)
plt.bar(x, y1)
plt.title("Bar Chart")

#  Scatter Plot
plt.subplot(2, 2, 3)
plt.scatter(x, y1)
plt.title("Scatter Plot")

#  Pie Chart
plt.subplot(2, 2, 4)
labels = ['A', 'B', 'C', 'D']
values = [10, 20, 30, 40]
plt.pie(values, labels=labels, autopct='%1.1f%%')
plt.title("Pie Chart")

plt.tight_layout()
plt.show()