import pandas as pd

# Load the data
file_path = 'C:\\Users\\91962\\Pictures\\Food Sales Analytics\\DataSet.xlsx' #load your dataset location here
data = pd.read_excel(file_path)

# Drop Unnecessary Columns
data = data.drop(columns=['Unnamed: 9', 'Unnamed: 10'], errors='ignore')

# Rename Columns (for consistency)
data.columns = data.columns.str.strip()  
data = data.rename(columns={
    'TransactionID': 'transaction_id',
    'Product': 'product',
    'Region': 'region',
    'Salesperson': 'salesperson',
    'Date': 'date',
    'Quantity': 'quantity',
    'Unit Price': 'unit_price',
    'Category': 'category',
    'Total Sales': 'total_sales'
})


print("Missing Values Before:\n", data.isnull().sum())

data = data.dropna(subset=['product', 'region', 'salesperson', 'date', 'quantity', 'unit_price', 'total_sales'])

data['total_sales'] = data['total_sales'].fillna(data['quantity'] * data['unit_price'])

print("Missing Values After:\n", data.isnull().sum())

duplicates = data.duplicated()
print("Number of Duplicates:", duplicates.sum())
data = data.drop_duplicates()

# 5. Convert Data Types (if necessary)
data['date'] = pd.to_datetime(data['date']) 
data['quantity'] = data['quantity'].astype(int)  
data['unit_price'] = data['unit_price'].astype(float)  
data['total_sales'] = data['total_sales'].astype(float)  

Q1 = data[['total_sales', 'quantity']].quantile(0.25)
Q3 = data[['total_sales', 'quantity']].quantile(0.75)
IQR = Q3 - Q1

data = data[~((data[['total_sales', 'quantity']] < (Q1 - 1.5 * IQR)) | (data[['total_sales', 'quantity']] > (Q3 + 1.5 * IQR))).any(axis=1)]

data = data.reset_index(drop=True)

# Display the cleaned data summary
print("Data Information After Cleaning:\n")
data.info()
print("\nFirst 5 Rows of Cleaned Data:\n", data.head())
