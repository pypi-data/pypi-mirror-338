import pandas as pd
import json
from pathlib import Path

# Get the parent directory of the current file's directory.
weather_wise_directory = Path(__file__).resolve().parent.parent

# Define the path to the csv file.
csv_path = weather_wise_directory / "data" / "2024_Gaz_zcta_national.csv"

# Load the csv file into a pandas DataFrame.
# dtype={"zipcode": str} ensures that the "zipcode" column is treated as a string.
# This is important for zip codes that may have leading zeros.
df = pd.read_csv(csv_path, dtype={"zipcode": str})

# Convert the DataFrame to a dictionary.
# Set the index to "zipcode" and convert to dictionary format.
data = df.set_index("zipcode").to_dict(orient="index")

# Define the path to the json file.
json_path = weather_wise_directory / "data" / "2024_Gaz_zcta_national.json"

# Save to JSON file
with open(json_path, "w") as file:
    json.dump(data, file, indent=4)
