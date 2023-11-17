import requests
import re
from config import NOAA_API_BASE_URL

def get_gridpoint_by_latlong(lat, long):
    url = f"{NOAA_API_BASE_URL}/points/{lat},{long}"
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"API request failed with status code {response.status_code}")
    grid_url = response.json()['properties']['forecast']
    gridpoint = re.findall('api.weather.gov/gridpoints/(\w+)(/)(\d+)(,)(\d+)', grid_url)
    return ''.join(gridpoint[0])

def get_nearest_station(gridpoint):
    url = f"{NOAA_API_BASE_URL}/gridpoints/{gridpoint}/stations"
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"API request failed with status code {response.status_code}")
    return response.json()['features'][0]['id'][32:37]

def get_weather_data(station, date):
    url = f"{NOAA_API_BASE_URL}/stations/{station}/observations?end={date}&limit=1"
    response = requests.get(url)
    if response.status_code != 200:
        raise Exception(f"API request failed with status code {response.status_code}")
    return response.json()['features'][0]['properties']