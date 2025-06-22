import os
import pandas as pd
#from dotenv import load_dotenv
from opencage.geocoder import OpenCageGeocode

#load_dotenv() #Used for local development
key = os.environ.get('OPENCAGE_API_KEY')
if not key:
    raise ValueError("Missing API key.")
geocoder = OpenCageGeocode(key)

racing_data = pd.ExcelFile("Garage 61 - Zak Groenewold - Statistics - 2025-06-15-17-20-02.xlsx") #Read entire file

"""Automate track_location fill-in"""
def check_track_locations(racing_data_path=racing_data, location_csv='track_locations.csv'): #Excel sheet must include sheet named "Popular tracks"
    track_locations = pd.read_csv(location_csv) 
    known_tracks = track_locations['track'].unique()
    
    tracks_driven_df = pd.read_excel(racing_data_path, sheet_name='Popular tracks') #Load list of tracks driven from sheet
    tracks_driven = tracks_driven_df['Track'].unique() #Clean list of driven tracks to iterate over
    
    for track in tracks_driven:
        if track not in known_tracks:
            try:
                results = geocoder.geocode(track)
            except Exception as e:
                print(f"Error finding {track}: {e}")
                continue
            if results:
                lat = results[0]["geometry"]["lat"]
                lng = results[0]["geometry"]["lng"]
                track_df = pd.DataFrame({'track':[track],
                                         'latitude':[lat],
                                         'longitude': [lng]})
                track_df.to_csv(location_csv, mode = 'a', header=False, index=False)
                print(track_df)

check_track_locations()