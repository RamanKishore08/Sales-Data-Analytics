import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the data
file_path = 'C:\\Users\\91962\\Pictures\\Food Sales Analytics\\DataSet.xlsx' #load your dataset directory here
data = pd.read_excel(file_path)

print("First 5 Rows of Data:\n", data.head())
print("\nData Information:\n")
data.info()
print("\nSummary Statistics:\n", data.describe())
print("\nMissing Values:\n", data.isnull().sum())
data = data.drop(columns=['Unnamed: 9', 'Unnamed: 10'], errors='ignore')


# Distribution of Total Sales
plt.figure(figsize=(10, 5))
sns.histplot(data['Total Sales'], kde=True, bins=30)
plt.title("Distribution of Total Sales")
plt.xlabel("Total Sales")
plt.ylabel("Frequency")
plt.show()

# Count of Products by Category
plt.figure(figsize=(10, 5))
sns.countplot(data=data, x='Category', order=data['Category'].value_counts().index)
plt.title("Product Count by Category")
plt.xlabel("Category")
plt.ylabel("Count")
plt.xticks(rotation=45)
plt.show()

# Sales by Region
plt.figure(figsize=(10, 5))
sns.barplot(data=data, x="Region", y="Total Sales", estimator=sum)
plt.title("Total Sales by Region")
plt.xlabel("Region")
plt.ylabel("Total Sales")
plt.show()

# Correlation Heatmap
plt.figure(figsize=(8, 6))
sns.heatmap(data.corr(), annot=True, cmap='coolwarm', fmt=".2f")
plt.title("Correlation Heatmap")
plt.show()

# Total Sales by Salesperson
plt.figure(figsize=(12, 6))
sns.barplot(data=data, x="Salesperson", y="Total Sales", estimator=sum, ci=None, order=data.groupby('Salesperson')['Total Sales'].sum().sort_values(ascending=False).index)
plt.title("Total Sales by Salesperson")
plt.xlabel("Salesperson")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.show()

# Quantity vs Total Sales Scatter Plot (for relationship insight)
plt.figure(figsize=(10, 5))
sns.scatterplot(data=data, x="Quantity", y="Total Sales", hue="Category")
plt.title("Quantity vs. Total Sales")
plt.xlabel("Quantity")
plt.ylabel("Total Sales")
plt.legend(title="Category")
plt.show()
