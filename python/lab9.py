#!/usr/bin/python3


import json

import requests


r = requests.get('http://localhost:3000' )

data = r.json()

##print(data['weather'][0]['description'])

print('')
print( data[0]['name'] + ' is ' + data[0]['color'] )
print('')
print( data[1]['name'] + ' is ' + data[1]['color'] )
print('')
print( data[2]['name'] + ' is ' + data[2]['color'] )
print('')
print( data[3]['name'] + ' is ' + data[3]['color'] )

