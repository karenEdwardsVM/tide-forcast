#!/usr/bin/env python3

import requests
import json
from bs4 import BeautifulSoup

def get_tides(city):
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
    places = ['Half-Moon-Bay-California', 'Huntington-Beach', 
              'Providence-Rhode-Island', 'Wrightsville-Beach-North-Carolina']
    return {city: find_city_tides(city) for city in places}

print(find_tides())
