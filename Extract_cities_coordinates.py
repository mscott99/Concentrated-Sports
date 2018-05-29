# -*- coding: utf-8 -*-
"""
Spyder Editor

Script to extract list of cities in Canada, along with their geographical coordinates

This is a temporary script file.
"""

import pandas as pd
from Sport_density import sport_density


class Extractor:

    sport_ID = ''
    list_of_cities_df = pd.read_csv('List_of_cities.csv')
    list_of_cities_df['Number_of_places'] = 0

    def __init__(self,sport):
        self.sport_ID = sport
    #Extract the list of cities
    #Helper function to extract density from latitude and longitude
    def extract_number_of_places(self, lon, lat, density_weighting=False):
        density_computation = sport_density(lat, lon, [self.sport_ID])
        density_computation.number_of_sport_places()
        return density_computation.number_sport_places[self.sport_ID]

    def get_most_popular_city(self):
        #Loop through all cities
        global list_of_cities_df
        Nb = []
        for i in range(len(self.list_of_cities_df)):
            Nb.append(self.extract_number_of_places(
                         self.list_of_cities_df['lng'].iloc[i], self.list_of_cities_df['lat'].iloc[i]))

        self.list_of_cities_df['Number_of_places'] = Nb

        self.list_of_cities_df.sort_values('Number_of_places', axis=0, ascending=False, inplace=True)

        city_with_most_places_coordinates = {}
        city_with_most_places_coordinates = self.list_of_cities_df[['lat','lng','city','Number_of_places']].iloc[0].to_dict()
        return city_with_most_places_coordinates
