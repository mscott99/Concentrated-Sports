# -*- coding: utf-8 -*-
"""
Created on Mon May 28 12:09:13 2018

Script to extract the number of sport places for a list of sports in a given
radius around a specific latitude/longitude. Extract the information
by querying the sport places API

@author: AI team
"""

import json
import requests

class sport_density():
    def __init__(self, lat, lon, list_of_sports, radius=50):
        self.lat = lat
        self.lon = lon
        self.list_of_sports = list_of_sports
        
    def number_of_sport_places(self, radius=50):
        self.radius = radius
        #We will extract the number of sport places in a dictionary
        self.number_sport_places = {}
        #Query the sport places API
        for i in self.list_of_sports:
            try:
                url = 'https://sportplaces-api.herokuapp.com/api/v1/places?origin={},{}&radius={}&sports={}'.format(self.lon,
                                                                                  self.lat, self.radius, int(i))
                response = requests.get(url)
                data = json.loads(response.text)
                self.number_sport_places[i] = len(data['features'])
            except:
                print('Could not find number of locations for sport {}'.format(int(i)))
                self.number_sport_places[i] = 0
            
        