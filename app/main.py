import pandas as pd
import noaa_api
import data_processing
import geocode_addresses
from config import api_key, input_csv, output_csv, final_geo_enriched_csv

def main():
    #Geocode the addresses
    geocode_addresses.add_latitude_and_longitude(api_key, input_csv, output_csv)

    geocoded_df = pd.read_csv(output_csv)
    weather_data = []

    #Loop through the geocoded addresses, find closest weather station, and get weather data for the timestamp
    for index, row in geocoded_df.iterrows():
        print(f"Processing Row Number: {index}")
        lat, long = row['Y'], row['X']
        raw_date = row['Date Occurred']
        event_date = raw_date.replace("+", "%2B").replace(":", "%3A")
        print(f"Inputs for this search are: longitude: {long}, Latitude: {lat}, Date: {raw_date}")

        try:
            gridpoint = noaa_api.get_gridpoint_by_latlong(lat, long)
            print(f"Found Closest Gridpoint as: {gridpoint}")

            nearest_station = noaa_api.get_nearest_station(gridpoint)
            print(f"Found Closest Weather Station: {nearest_station}")

            weather_data_record = noaa_api.get_weather_data(nearest_station, event_date)
            cleaned_record = data_processing.process_weather_data(weather_data_record)

            weather_data.append(cleaned_record)
        except Exception as e:
            print(f"Error processing row {index}: {e}")

    final_weather_df = pd.concat(weather_data, axis=0, ignore_index=True, sort=False)

    final_df = data_processing.merge_dataframes(geocoded_df, final_weather_df)

    final_df.to_csv(final_geo_enriched_csv, index=False)
    print("Processing complete.")

if __name__ == "__main__":
    main()