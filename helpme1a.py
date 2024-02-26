import pandas as pd

def load_csv_data(file_path):
    return pd.read_csv(file_path)

def store_as_text(data, output_file_path):
    with open(output_file_path, "w") as file:
        file.write(data.to_csv(header=True, index=False))
        
        
csv_data = load_csv_data("D:/COLLEGE/PRACTICAL SEM 1/DAV PRACT/100 Sales Records.csv")       

def print_file_contents(file_path): 
    with open(file_path, "r") as file:
       contents = file.read()
       print(contents)
       
def display_data(data): 
    print(data.head())


store_as_text(csv_data, "store_csv_Data_in_text.txt")
print_file_contents("store_csv_Data_in_text.txt")
display_data(csv_data)