#!/usr/bin/python3


import json

import requests


print('please enter your zip code')

zip = input()

r = requests.get('http://api.openweathermap.org/data/2.5/weather?zip=%s,us&appid=e4e4444dc188871deb2a99d2e56faef8' % zip )

data = r.json()

print(data)

##print(data['weather'][0]['description'])
