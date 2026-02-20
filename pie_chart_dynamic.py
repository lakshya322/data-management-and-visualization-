import matplotlib.pyplot as plt
import numpy as np

x= input("Enter X values:").split()
y= list(map(int,input("Enter Y values:").split()))

y=np.array(y)

plt.pie(y, labels=x, autopct='%1.1f%%')

plt.title("dynamic pie chart")

plt.show()