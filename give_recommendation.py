# -*- coding: utf-8 -*-
"""
Created on Tue May 29 18:46:48 2018

@author: sam
"""

import json
import pandas as pd
import requests

sport_ID = '175'
lat = 45.52305
lon = -73.58139649999998  
radius = 50

#Get the sports recommended 
url = 'https://sportplaces-api.herokuapp.com/api/v1/recommendations/sport?sport={}&count={}'.format(int(sport_ID), 50)
response = requests.get(url)
data = json.loads(response.text)


#Translate the IDs to names
Sport_ID_df = pd.read_csv('Sport_ID_map.csv', encoding='latin1')
Sport_ID_dictionary = {}
for index, row in Sport_ID_df.iterrows():
    Sport_ID_dictionary[row['Sport,id'].split(',')[1]]=row['Sport,id'].split(',')[0]
    
count = 0
sports_recommended = []
for i in data:
    #Verify is their is a sport place
    url = 'https://sportplaces-api.herokuapp.com/api/v1/places?origin={},{}&radius={}&sports={}'.format(lon,
                                                                                  lat, radius, int(i))
    response = requests.get(url)
    data = json.loads(response.text)
    if len(data['features']) > 0:
        sports_recommended.append(i)
        count+=1
    
    if count == 3:
        break
    
if len(sports_recommended) < 3:        
    sports_recommended = [Sport_ID_dictionary[i] for i in data]
    
sports_recommended_dict = {}
sports_recommended_dict['Sports ID'] = sports_recommended
sports_recommended_dict['Sports name'] = [Sport_ID_dictionary[i] for i in sports_recommended]

print(json.dumps(sports_recommended_dict))
    
