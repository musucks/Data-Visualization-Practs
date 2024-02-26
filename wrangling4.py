import pandas as pd 
import numpy as np 
import os

data = {
"Transaction_ID": [1, 2, 3, 4, 5], "Product": ["A", "B", "C", "A", "B"], "Quantity": [10, -5, 20, 15, 8],
"Price": [15.0, 20.0, 25.0, None, 30.0],
"Date": ["2023-01-01", "2023-01-02", "2023-01-03", "2023-01-04", "2023-01-05"],
}

df = pd.DataFrame(data)
print(f"Task 1: Loaded Dataset\n{df.head()}")

missing_cols = df.columns[df.isnull().any()] 
df.fillna(0, inplace=True)
print(f"\nTask 2: Missing Values - After Handling\n{df}")
numeric_cols = df.select_dtypes(include=[np.number]).columns 
df[numeric_cols] = df[numeric_cols].abs()

print(f"\nTask 3: Negative Values - After Handling\n{df}")
df["Date"] = pd.to_datetime(df["Date"])

print(f"\nTask 4: Converted 'Date' column to DateTime format\n{df}")
df["Day"] = df["Date"].dt.day
df["Month"] = df["Date"].dt.month
df["Year"] = df["Date"].dt.year
print(f"\nTask 5: Extracted day, month, and year information from 'Date'\n{df}")
df["Total Sales"] = df["Quantity"] * df["Price"] 
print(f"\nTask 6: Calculated 'Total Sales'\n{df}")
grouped_df = (df.groupby("Product").agg({"Quantity": "sum", "Total Sales": "sum"}).reset_index()) 
print(f"\nTask 7: Grouped and Aggregated Data by 'Product'\n {grouped_df}")
wrangled_file_path = os.path.abspath("wrangled_dataset.csv") 
df.to_csv(wrangled_file_path, index=False)
print("\nTask 8: Saved the wrangled Dataset to ", wrangled_file_path)
transformed_file_path = os.path.abspath("transformed_dataset.csv") 
df.to_csv(transformed_file_path, index=False)
print("\nTask 9: Saved the Transformed Dataset to ", transformed_file_path)
transposed_df = df.transpose()

transposed_file_path = os.path.abspath("transposed_dataset.csv") 
transposed_df.to_csv(transposed_file_path, header=False)
print("\nTask 10: Transposed Dataset and Saved to ", transposed_file_path)
print("\nExample using iloc: ") 
selected_rows = df.iloc[1:3] 
selected_columns = df.iloc[:, [0, 2, 4]] 
print(f"Selected Rows: \n{selected_rows}")
print(f"Selected Columns: \n{selected_columns}")
sorted_df = df.sort_values(by="Total Sales", ascending=False) 
print("\nExample of Sorting by 'Total Sales' in Descending Order:") 
print(sorted_df)
