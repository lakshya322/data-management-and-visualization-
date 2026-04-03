import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

#Dataset

df = pd.read_csv(r"C:\Users\lab\Downloads\sample.csv")
# Bar chart
spending_cols = [
    'MntWines', 'MntFruits', 'MntMeatProducts',
    'MntFishProducts', 'MntSweetProducts', 'MntGoldProds'
]

df[spending_cols].mean().plot(kind='bar', color='skyblue')
plt.title("Average Spending by Category")
plt.ylabel("Amount")
plt.xticks(rotation=45)
plt.show()

# Line chart
df_sorted = df.sort_values(by='Income')

plt.plot(df_sorted['Income'], df_sorted['MntWines'], label='Wines')
plt.plot(df_sorted['Income'], df_sorted['MntMeatProducts'], label='Meat')

plt.title("Income vs Spending Trends")
plt.xlabel("Income")
plt.ylabel("Spending")
plt.legend()
plt.show()

# Pie chart

df_sorted = df.sort_values(by='Income')

plt.plot(df_sorted['Income'], df_sorted['MntWines'], label='Wines')
plt.plot(df_sorted['Income'], df_sorted['MntMeatProducts'], label='Meat')

plt.title("Income vs Spending Trends")
plt.xlabel("Income")
plt.ylabel("Spending")
plt.legend()
plt.show()

# line chart

totals = df[spending_cols].sum()

plt.pie(totals, labels=totals.index, autopct='%1.1f%%')
plt.title("Spending Distribution")
plt.show()



plt.step(df_sorted['Income'], df_sorted['MntWines'], where='mid')
plt.title("Stair Chart: Income vs Wine Spending")
plt.xlabel("Income")
plt.ylabel("Wine Spending")
plt.show()

plt.hist(df['Income'], bins=10, color='orange', edgecolor='black')
plt.title("Income Distribution")
plt.xlabel("Income")
plt.ylabel("Frequency")
plt.show()

missing = df.isnull().sum()
print("Missing Values:\n", missing)

# Visual heatmap
sns.heatmap(df.isnull(), cbar=False, cmap='viridis')
plt.title("Missing Values Heatmap")
plt.show()

plt.figure(figsize=(10,5))
sns.boxplot(data=df[spending_cols])
plt.title("Outliers in Spending Features")
plt.xticks(rotation=45)
plt.show()

Q1 = df.quantile(0.25)
Q3 = df.quantile(0.75)
IQR = Q3 - Q1

outliers = df[((df < (Q1 - 1.5 * IQR)) | (df > (Q3 + 1.5 * IQR))).any(axis=1)]

print("Outliers detected:")
print(outliers)
