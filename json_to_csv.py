import pandas as pd 
import json
import ast

def json_to_csv(json_file_path, csv_file_path):
    # Load JSON data
    with open(json_file_path, 'r') as file:
        try:
            data = json.load(file)
            data = ast.literal_eval(data)
        except json.JSONDecodeError as e:
            raise ValueError(f"Error decoding JSON file: {e}")
    
    # Check the type of data and normalize accordingly
    if isinstance(data, list):
        # Case 1: JSON is a list of dictionaries
        df = pd.json_normalize(data)
    
    elif isinstance(data, dict):
        # Case 2: JSON is a dictionary of dictionaries
        # Convert dictionary to a list of dictionaries
        data_list = [{'key': k, **v} for k, v in data.items()]
        df = pd.json_normalize(data_list)
    
    else:
        raise ValueError("Unsupported JSON format. The JSON must be a list of objects or a dictionary of objects.")
    
    # Write the DataFrame to a CSV file
    df.to_csv(csv_file_path, index=False)

# Example usage
json_file_path = 'package_descriptions.json'  # Replace with your JSON file path
csv_file_path = 'output_file.csv'           # Replace with your desired CSV file path
json_to_csv(json_file_path, csv_file_path)
