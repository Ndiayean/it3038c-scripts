#!/usr/bin/python3


import json

import requests


print('please enter your zip code')

zip = input()

##Removed Api key 
r = requests.get('http://api.openweathermap.org/data/2.5/weather?zip=%s,us&appid=yourapikey' % zip )

data = r.json()

print(data)

##print(data['weather'][0]['description'])
