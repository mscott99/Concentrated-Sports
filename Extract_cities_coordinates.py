# -*- coding: utf-8 -*-
"""
Spyder Editor

Script to extract list of cities in Canada, along with their geographical coordinates

This is a temporary script file.
"""

import pandas as pd
from Sport_density import sport_density

sport_ID = '175'

#Extract the list of cities
list_of_cities_df = pd.read_csv('List_of_cities.csv')
list_of_cities_df['Number_of_places'] = 0

#Helper function to extract density from latitude and longitude
def extract_number_of_places(sport_ID, lon, lat, density_weighting=False):
    density_computation = sport_density(lat, lon, [sport_ID])
    density_computation.number_of_sport_places()
    return density_computation.number_sport_places[sport_ID]

#Loop through all cities
Nb = []
for i in range(len(list_of_cities_df)):  
    Nb.append(extract_number_of_places(sport_ID, 
                 list_of_cities_df['lng'].iloc[i], list_of_cities_df['lat'].iloc[i]))

list_of_cities_df['Number_of_places'] = Nb

list_of_cities_df.sort_values('Number_of_places', axis=0, ascending=False, inplace=True)

city_with_most_places_coordinates = {}
city_with_most_places_coordinates['lat'] = list_of_cities_df['lat'].iloc[0]
city_with_most_places_coordinates['lon'] = list_of_cities_df['lng'].iloc[0]