#!/usr/bin/python3

##This is a script that will help us perform network and security tasks


import socket

##This part of the script will grab the IP address of each of the domains in the list and print it on the console
hosts = ['www.uc.edu', 'www.google.com', 'www.bing.com']

## This will print out the current machine name 
print ('Working from host: ' + socket.getfqdn())

##Note socket.getfqdn() without any parameters will display the current hosts inforrmation

##This will match the host name with the IP address
for h in hosts:
    print(h + ': ' + socket.gethostbyname(h))
