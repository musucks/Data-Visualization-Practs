
import json
import pandas as pd

def load_json_data(file_path):
    with open(file_path, "r") as file:
        data = json.load(file)
    return pd.json_normalize(data)
    
def store_as_text(data, output_file_path):
    with open(output_file_path, "w") as file:
        file.write(data.to_csv(header=True, index=False))
        
def print_file_contents(file_path):
    with open(file_path, "r") as file:
        content = file.read()
        print(content)

json_data = load_json_data("D:/COLLEGE/PRACTICAL SEM 1/DAV PRACT/sample.json")
store_as_text(json_data, "json_data_in_text.txt")
print_file_contents ("json_data_in_text.txt")