import pandas as pd

def load_excel_data(file_path, sheet_name=0):
    return pd.read_excel(file_path, sheet_name=sheet_name)

def store_as_text(data, output_file_path):
    with open(output_file_path, "w") as file:
        file.write(data.to_csv(header=True, index=False))
        
def print_file_contents(file_path):
    with open(file_path, "r") as file:
        contents = file.read()
        print(contents)
        
def display_data(data):
    print(data.head())
    
excel_data = load_excel_data("D:/COLLEGE/PRACTICAL SEM 1/DAV PRACT/100 Sales RecordsS.xlsx")

store_as_text(excel_data, "excel_Data_in_text.txt")
print_file_contents("excel_Data_in_text.txt")
display_data(excel_data)
