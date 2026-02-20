import matplotlib.pyplot as plt

x= ['maths','english','science','hindi']
y= [10,20,30,40]

plt.pie(y, labels=x, autopct='%1.1f%%')

plt.title("static pie chart")

plt.show()