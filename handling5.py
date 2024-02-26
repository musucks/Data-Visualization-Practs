import pandas as pd 
data = {
"ID": [1, 2, 3, 4, 5],
"Name": ["Alice", "Bob", "Charles", "David", "Eva"], "Age": [25, 32, None, 28, 22],
"Grade": ["A", "B", "C", None, "A"],
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

df["Grade"].fillna("Unknown", inplace=True)
print(f"\nTask 3: Handled Missing Data\n{df}")
df["Name"] = df["Name"].str.upper()
print(f"\nTask 4: Converted Names to UpperCase\n{df}")
df["City_First_Letter"] = df["City"].str[0]

print(f"\nTask 5: Extracted First Letter of City\n{df[['ID', 'City', 'City_First_Letter']]}")
processed_file_path = "processed_dataset.csv"
df.to_csv(processed_file_path, index=False)
print(f"\nTask 6: Saved the Processed Dataset to {processed_file_path}")

df["City_No_Spaces"] = df["City"].str.replace(" ", "")
print(f"\nTask 7: Replaced Spaces in City Names\n{df[['ID','City', 'City_No_Spaces']]}")
df["Has_Substring_LA"] = df["City"].str.contains("LA")
print(f"\nTask 8: Checked for Substring 'LA' in City Names\n{df [['ID', 'City', 'Has_Substring_LA']]}")

df[["First_Name", "Last_Name"]] = df["Name"].str.extract(r"(?P<First_Name>\S+)(?:\s+(?P<Last_Name>\S+))?", expand=True ) 
print(f"\nTask 9: Extracted First and Last Name\n{df [['ID', 'Name', 'First_Name', 'Last_Name']]}")
df["Full_Name"] = df["Name"]

df = df.drop("Name", axis=1)
print(f"\nTask 10: Joined First and Last Name\n{df [['ID', 'First_Name', 'Last_Name', 'Full_Name']]}")
df["Grade_Digits"] = df["Grade"].str.extract(r"(\d+)", expand=False)

print(f"\nTask 11: Extracted Digits from Grade\n{df [['ID', 'Full_Name','Grade', 'Grade_Digits']]}")
df["Vowel_Count"] = df["City"].str.count(r"[aeiouAEIOU]")

print(f"\nTask 12: Counted vowels in City Names\n{df [['ID', 'City', 'Vowel_Count']]}")
updated_file_path = "updated_dataset.csv" 

df.to_csv(updated_file_path, index=False)
print(f"\nTask 13: Saved the Updated Dataset to {updated_file_path}")
