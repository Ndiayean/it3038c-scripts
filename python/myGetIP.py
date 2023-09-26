#!/usr/bin/python3

##This script will use the input from the terminal to find an IP address

import socket, sys

def getHostnameByIP(h):


##We can catch any potential errors by using a try accept statment, for errors such as putting in a bad hostname

    try:

## an argument is anything you enter in the terminal that is seperated by a space
##sys.argv[1] is the second argument that we typed in the terminal
##py is ommited because its the interpreter that we are specifying
## Example: py myGetIP.py value
##sys.argv[0]= myGetIP.py  and sys.argv[1]= value and so on 
##The first argument when invoking the script is always the script name

##    hostname = str(sys.argv[1])
        hostname = str(h)

        IP = socket.gethostbyname(hostname)

        print (hostname + ' has an IP of ' + IP)

    except:
        print("Oops, something is wrong with that host")

## To try this program do myGetIP.py google.com           or any hostname
## myGetIP.py would be sys.argv[0] and google.com would be sys.argv[1]

##Now we can call the from within the script and store those values in variables
##The function we created above wont do anything unless its invoked in the script
##Then the contents within the function will be executed based on the parameters we passed
getHostnameByIP(sys.argv[1])
