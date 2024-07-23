from google_play_scraper import app # type: ignore
import pandas as pd

# Function to scrape data for a given package name
def scrape_app_data(package_name):
    try:
        result = app(package_name)
        return result
    except Exception as e:
        print(f"Failed to scrape data for {package_name}: {e}")
        return None

# # Example usage
package_names = ['com.lexa.fakegps', 'com.locationchanger', 'com.fly.gps']  # Replace with actual package names

app_data = [scrape_app_data(pkg) for pkg in package_names]

# # Filter out None values from the list
# app_data = [data for data in app_data if data is not None]

# # Print the keys of the scraped data
# print(app_data[0].keys())
# # Print the scraped data
for data in app_data:
    print(data)

df = pd.DataFrame(app_data)

# Save the DataFrame to a CSV file
df.to_csv("app_data5.csv", index=False)