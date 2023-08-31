#!/bin/bash

#This script will output the IP address and Hostname of a machine for the
#connection called "enp0s3" if it exists

ip a | grep "noprefixroute enp0s3" | awk '{print $2}'

#using a variable on an echo function

greeting="This is my script . Hello!"
#
#
#
#
echo $greeting, thanks for joining us!
echo $greeting, thanks for joining us! You owe me \$20
echo '$greeting, thanks for joining us! You owe me $20'
echo "$greeting, thanks for joining us!"
echo "$greeting, you owe me \$20"
#
#
#
#

#machine details outputed on terminal

echo Machine Type: $MACHINETYPE
echo Hosname: $HOSTNAME
echo Working Dir: $PWD
echo Session length: $SECONDS
echo Home Dir: $HOME
#
#
#
#
echo " "
echo " "


# IP address stored as a variable then outputed on terminal

a=$(ip a | grep 'noprefixroute enp0s3'| awk '{print $2}')
echo My IP is $a


