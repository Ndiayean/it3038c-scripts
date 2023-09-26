#!/usr/bin/python3

import time
##This is the current time that I started the program
start_time = time.time()

##This page is going to take inputs from teh users and return them in the shell

print('what is your name?')

myName = input()

print('Hello, ' + myName + '. That is a good name. How old are you?')

myAge = input()

##This is how much time durated since the program started
programAge = int(time.time() - start_time)

print('%s? That\'s funny, I\'m only a %s seconds old' % (myAge, programAge))

##This would output the input of myAge as a string and duplicate it twiche
##print('I wish I was ' + myAge * 2 + 'years old')

##To use input as a number you have to cast it using the int(inputname).Then cast it back into a string so that we can concat it to the other strings.
print('I wish I was ' + str(int(myAge) * 2) + ' years old')

##You can also store the value of my Age from a string input to a number from the myAge variable

##myAge = int(input()

##Then all we would need is to add the str() cast within the print statement to change the number to a string

##You can also variable substition within a string by using %s as the placeholder
print ('What is your age again')
myAge = int(input())


print('Wait! %s?????' % (myAge*2))
print('Oh!!  I thought you said you were %s' % (myAge ))


##This pauses the script for 3 seconds and continues rest. to use this import the 'time' module at the top from the python standard library

time.sleep(3)

print('I\'m tired. I go to sleep sleep now.')





## to run the code in linux use the command: python3 filename
## Since I already specified the interpreter at the top you also just use ./filename given that you already setup executable permissions for the file


