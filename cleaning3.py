
import pandas as pd
from scipy.stats import zscore
data = {
    "ID": [1, 2, 3, 4, 5],
    "Name": ["Alice", "Bob", "Charles", "David", "Eva"], 
    "Age": [25, 32, None, 28, 22],
    "Salary": [50000, 60000, 75000, None, 45000],
    "City": ["New York", "San Francisco", "Los Angeles", "Chicago", "Miami"],
}
df = pd.DataFrame(data) 
print("\nTask 1: Loaded Dataset") 
print(df.head())

missing_cols = df.columns[df.isnull().any()] 
missing_percentage = df[missing_cols].isnull().mean() * 100
print("\nTask 2: Missing Values")
print("Columns with missing values: ", list(missing_cols)) 
print("Percentage of missing values: ", missing_percentage)

df["Age"].fillna(df["Age"].mean(), inplace=True) 
df["Salary"].fillna(df["Salary"].median(), inplace=True) 
print("\nTask 3: Handled Missing Data")

df.drop_duplicates(inplace=True) 
print("Task 4: Removed Duplicate Entries") 
print(df)

df["Age"] = df["Age"].astype(int) 
df["Salary"] = df["Salary"].astype(float) 
print("\nTask 5: Converted Data Types") 
print(df.dtypes)

unique_cities = df["City"].unique() 
df["City"] = pd.Categorical(df["City"]) 
print("\nTask 6: Explored Categorical Data") 
print("Unique Cities: ", unique_cities)
df_outliers = df.copy() 

numeric_columns = ["Age", "Salary"]
z_scores = zscore(df_outliers[numeric_columns]) 
threshold = 3
outliers = (abs(z_scores) > threshold).any(axis=1) 
df_outliers = df_outliers[~outliers]

print("\nTask 7: Handling Outliers using Z-score") 
print("Rows with outliers removed:") 
print(df_outliers)


#pip install beautifulsoup4 requests
#pip install requests beautifulsoup4 lxml#
#python3 -m pip install lxm