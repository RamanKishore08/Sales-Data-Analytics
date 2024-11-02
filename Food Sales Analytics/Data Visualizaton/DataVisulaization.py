import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

# Load the Excel file
file_path = 'C:\\Users\\91962\\Pictures\\Food Sales Analytics\\DataSet.xlsx'
data = pd.read_excel(file_path)


data_cleaned = data.drop(columns=['Unnamed: 9', 'Unnamed: 10'])

# Seaborn style
sns.set(style="whitegrid")

# Create a bar plot for total sales by category and region
plt.figure(figsize=(12, 6))
sns.barplot(data=data_cleaned, x="Category", y="Total Sales", hue="Region", ci=None)
plt.title("Total Sales by Product Category and Region")
plt.xlabel("Product Category")
plt.ylabel("Total Sales")
plt.legend(title="Region")
plt.xticks(rotation=45)
plt.tight_layout()

# Show the visualization
plt.show()
