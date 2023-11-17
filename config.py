from dotenv import load_dotenv
import os

#%%
load_dotenv()

#%%

api_key = os.getenv('api_key', "")
input_csv = 'addresses_and_timestamps.csv'
output_csv = 'addresses_geocoded_and_timestamped.csv'

NOAA_API_BASE_URL = "https://api.weather.gov"

final_geo_enriched_csv = 'addresses_geocoded_and_timestamped_and_weather.csv'