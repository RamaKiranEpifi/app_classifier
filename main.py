import pandas as pd
import json
from google_play_scraper import app
import json

# Function to extract top N rows of a specific column from a file
def extract_top_n_column_to_list(file_path, sheet_name='Sheet1', column_name='Package_name', n=100):
    # Determine the file extension
    file_extension = file_path.split('.')[-1].lower()
    
    # Read the file based on its extension
    if file_extension in ['xls', 'xlsx']:
        df = pd.read_excel(file_path, sheet_name=sheet_name)
    elif file_extension == 'csv':
        df = pd.read_csv(file_path)
    else:
        raise ValueError("Unsupported file format. Please provide a .xls, .xlsx, or .csv file.")
    
    print(df.columns)

    # Check if the specified column exists
    if column_name not in df.columns:
        raise ValueError(f"Column '{column_name}' does not exist in the file.")
    
    # Extract the top N rows of the column and convert it to a list
    column_data = df[column_name].head(n).tolist()
    
    return column_data

# Function to scrape data for a given package name
def scrape_app_data(package_name):
    try:
        result = app(package_name)
        return result.get('description', 'No description available')
    except Exception as e:
        print(f"Failed to scrape data for {package_name}: {e}")
        return 'Error fetching description'

# Function to create a JSON file with package names and descriptions
def create_json_from_top_n_package_names(input_file_path, output_json_file, sheet_name='Sheet2', column_name='Package_name', n=100):
    # Extract top N package names
    package_names = extract_top_n_column_to_list(input_file_path, sheet_name, column_name, n)
    
    # Scrape data for each package name
    package_descriptions = {}
    for package_name in package_names:
        description = scrape_app_data(package_name)
        package_descriptions[package_name] = description
    
    # Write the data to a JSON file
    with open(output_json_file, 'w') as json_file:
        json.dump(package_descriptions, json_file, indent=4)

df = pd.read_json('package_descriptions.json')
print(df)
df.to_csv('package_descriptions.csv', index = False)

# Example usage
input_file_path = 'Sheet1.csv'  # Change this to your file path
output_json_file = 'package_descriptions.json'  # Output JSON file
# create_json_from_top_n_package_names(input_file_path, output_json_file)
