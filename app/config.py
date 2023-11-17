from dotenv import load_dotenv
import os

#%%
load_dotenv()

# Get the directory of the config.py file
config_dir = os.path.dirname(os.path.abspath(__file__))

# Go up one level to the root directory
root_dir = os.path.dirname(config_dir)

# Construct the path to the data folder
data_dir = os.path.join(root_dir, 'data')

#%%

api_key = os.getenv('api_key', "")
input_csv = os.path.join(data_dir,'addresses_and_timestamps.csv')
output_csv = os.path.join(data_dir,'addresses_geocoded_and_timestamped.csv')

NOAA_API_BASE_URL = "https://api.weather.gov"

final_geo_enriched_csv = os.path.join(data_dir,'addresses_geocoded_and_timestamped_and_weather.csv')