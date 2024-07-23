import pandas as pd 
import json
import ast

def collect_keys(data, level=0, keys_by_level=None):
    if keys_by_level is None:
        keys_by_level = {}
    
    if level not in keys_by_level:
        keys_by_level[level] = set()
    
    if isinstance(data, dict):
        for key, value in data.items():
            keys_by_level[level].add(key)
            collect_keys(value, level + 1, keys_by_level)
    elif isinstance(data, list):
        for item in data:
            collect_keys(item, level, keys_by_level)
    
    return keys_by_level

input_file_path = 'package_descriptions.json'
nested_json = pd.read_json(input_file_path)
# Collect keys layer by layer
keys_by_level = collect_keys(nested_json)

# Convert the collected keys to a DataFrame
data = {"Level": [], "Keys": []}
for level, keys in keys_by_level.items():
    data["Level"].append(level)
    data["Keys"].append(", ".join(keys))

df = pd.DataFrame(data)

# Save the DataFrame to a CSV file
df.to_csv('keys_by_level.csv', index=False)

# Display the DataFrame
print(df)