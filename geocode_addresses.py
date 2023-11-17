import pandas as pd
import requests
from config import api_key,input_csv,output_csv

def add_latitude_and_longitude(api_key, input_csv, output_csv):
    """
    Geocode addresses from an input CSV file and save the results to an output CSV file.

    Parameters:
        api_key (str): Your Google Maps Geocoding API key.
        input_csv (str): Path to the input CSV file containing addresses.
        output_csv (str): Path to save the geocoded results.
    """
    # Load the CSV file into a DataFrame
    df = pd.read_csv(input_csv)

    # Assuming 'address' is the column name with addresses. Adjust as necessary.
    latitudes = []
    longitudes = []

    for address in df['address']:
        response = requests.get(f'https://maps.googleapis.com/maps/api/geocode/json?address={address}&key={api_key}')
        resp_json_payload = response.json()

        if 'error_message' in resp_json_payload:
            print(f"Error geocoding {address}: {resp_json_payload['error_message']}")
            latitudes.append(None)
            longitudes.append(None)
            continue

        try:
            lat = resp_json_payload['results'][0]['geometry']['location']['lat']
            lon = resp_json_payload['results'][0]['geometry']['location']['lng']
        except IndexError:
            print(f"Error geocoding {address}: No result found.")
            lat = None
            lon = None

        latitudes.append(lat)
        longitudes.append(lon)

    df['latitude'] = latitudes
    df['longitude'] = longitudes
    df.to_csv(output_csv, index=False)
    print(f"Geocoding completed. Results saved to {output_csv}")