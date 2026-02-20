import numpy as np
import matplotlib.pyplot as plt

# Generate random data
data = np.random.normal(loc=50, scale=10, size=1000)

# Create histogram
plt.hist(data, bins=20, color='skyblue', edgecolor='black')

# Labels and title
plt.title("Static Histogram")
plt.xlabel("Value")
plt.ylabel("Frequency")

# Show plot
plt.show()