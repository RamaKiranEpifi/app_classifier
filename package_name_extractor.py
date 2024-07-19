import pandas as pd

def extract_column_to_list(file_path, sheet_name='Sheet1', column_name='Package_name'):
    # Determine the file extension
    file_extension = file_path.split('.')[-1].lower()
    
    # Read the file based on its extension
    if file_extension in ['xls', 'xlsx']:
        df = pd.read_excel(file_path, sheet_name=sheet_name)
    elif file_extension == 'csv':
        df = pd.read_csv(file_path)
    else:
        raise ValueError("Unsupported file format. Please provide a .xls, .xlsx, or .csv file.")
    
    # Check if the specified column exists
    if column_name not in df.columns:
        raise ValueError(f"Column '{column_name}' does not exist in the file.")
    
    # Extract the column and convert it to a list
    column_data = df[column_name].tolist()
    
    return column_data

# Example usage
file_path = 'path_to_your_file.xlsx'  # Change this to your file path
column_data = extract_column_to_list(file_path)
print(column_data)
