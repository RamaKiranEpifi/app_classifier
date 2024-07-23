import json
import csv

def inp_csv(input_path, csv_file='input.csv'):
    
    with open(input_path, 'r', encoding='utf-8') as file:
        data = json.load(file)

    # Open the CSV file for writing
    with open(csv_file, mode='w', newline='', encoding='utf-8') as file:
        writer = csv.writer(file)
        
        # Write the header
        writer.writerow(['Key', 'Description'])
        
        # Write the data
        for key, value in data.items():
            writer.writerow([key, value])
        
        print(f'Data has been written to {csv_file}')


inp_csv('package_descriptions.json')



