#!/usr/bin/env python3

import requests
import json
from bs4 import BeautifulSoup

def get_tides(city):
    '''Requests a url for a particular city, and parses the html to JSON'''
    url = 'https://www.tide-forecast.com/locations/'
    try:
        req = requests.get(url + city + '/tides/latest')
        html_content = BeautifulSoup(req.content, 'html.parser')
        tide_str = [str(s) for s in html_content.find_all('script') 
                           if str(s).__contains__('window.FCGON')][0]
        start = tide_str.find('{')
        end = tide_str.find('};') + 1
        tide_str = tide_str[start:end]
        return json.loads(tide_str)
    except:
        raise Exception("Couldn't fetch tides for " + city)

def find_city_tides(city):
    '''Finds the tides for a city that are after sunrise and before sunset'''
    tide_data = get_tides(city)
    low_tides = [[e['date'], t] 
                 for e in tide_data['tideDays'] 
                 for t in e['tides'] 
                 if t['type'] == 'low' and 
                    t['timestamp'] > e['sunrise'] and 
                    t['timestamp'] < e['sunset']]
    return [{'date': e[0], 
             'time': e[1]['time'], 
             'height': e[1]['height']} for e in low_tides]

def find_tides():
    '''Finds the tide information for each city in the list'''
    places = ['Half-Moon-Bay-California', 'Huntington-Beach', 
              'Providence-Rhode-Island', 'Wrightsville-Beach-North-Carolina']
    return {city: find_city_tides(city) for city in places}

tides = find_tides()

for city in tides:
    print('\n' + city + ':')
    for t in tides[city]:
        print('date:', t['date'], 'time:', t['time'], ' height:', t['height'])
