# Car Accidents and Weather Data Enrichment Project

## Goal
This project aims to enrich a list of car accidents, characterized by addresses and timestamps, with weather data obtained from the NOAA's Weather API.

## Project Operations
The project consists of the following steps:

1. **Address Processing**:
   - Reads a list of car accident addresses and timestamps.
   - Tags each address with latitude and longitude using the Google Maps API.
   - Saves the data as a CSV file.

2. **Weather Data Enrichment**:
   - Iterates through each row of the CSV, performing the following:
     - Prints the current processing row number.
     - Queries the NOAA's Weather API to find the nearest weather grid point based on latitude and longitude.
     - Identifies the nearest weather observation station using the grid point.
     - Retrieves the weather data for the specific date from the weather station.
     - Cleans and formats the weather data, including selecting and renaming columns, handling missing values, and structuring the data into a DataFrame.

3. **Data Integration**:
   - Combines the cleaned weather data with the original CSV data.

4. **Final Output**:
   - Saves the enriched data as 'DataEnrichedWithWeather.csv' on the user's desktop.

## Setup Instructions
1. Clone the project repository.
2. Open a terminal, navigate to the project folder, and run `poetry install` to install dependencies.
3. If using PyCharm, update the project interpreter to the poetry virtual environment. Otherwise, activate the virtual environment by running `poetry shell`.
4. Update the `.env example` file with your Google Maps API key. [Get a Google Maps API key](https://developers.google.com/maps/documentation/geocoding/get-api-key).
5. Modify the `addresses_and_timestamps.csv` file with your data.
6. Run the script with `poetry run python main.py` in the terminal to generate the output file.