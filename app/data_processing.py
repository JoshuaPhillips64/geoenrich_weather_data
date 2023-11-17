import pandas as pd

def process_weather_data(record):
    # Process and clean the weather data
    record_df = pd.DataFrame({key: pd.Series(value) for key, value in record.items()})

    record_df.drop(labels=['@id', '@type', 'rawMessage', 'icon', 'presentWeather', 'maxTemperatureLast24Hours',
                           'minTemperatureLast24Hours', 'cloudLayers'], axis=1, inplace=True)

    record_df.drop(labels=['qualityControl', 'unitCode'], axis=0, inplace=True)

    record_df = record_df.apply(lambda x: x.dropna().reset_index(drop=True))

    record_df = record_df.rename(columns={
        'elevation': 'elevation(meters)', 'temperature': 'temperature(C)', 'dewpoint': 'dewpoint(C)',
        'windDirection': 'windDirection(degree angle)', 'windSpeed': 'windSpeed(Km//h)',
        'barometricPressure': 'barometricPressure(Pa)', 'visibility': 'visibility(meters)',
        'heatIndex': 'heatIndex(C)', 'textDescription': 'WeatherDescription',
        'timestamp': 'Closest Timestamp to Occurrence', 'station': 'Closest Weather Station'
    })
    return record_df

def merge_dataframes(cbp_df, weather_df):
    return pd.concat([cbp_df, weather_df], axis=1)