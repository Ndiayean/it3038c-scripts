#!/usr/bin/python3


import os

##Welcomes user
print('#################################')
print('   Welcome to the file analyzer')
print('#################################')
##It will create the files in the C drive
path = '/'

##It will move the user to the C folder
os.chdir(path)

filesfolder = 'Testfiles'

##Create the file called "testfile" in the current directory
os.makedirs(filesfolder)


##Creates spaces
print('')
print('')

os.chdir(path + '/' + filesfolder)
##It will prompt the user to enter their name
name = input("What is your name")

## creating several files to store content

with open('Studentslist.txt', 'w') as f:
    ## variable name is not showing
    ## only string {name} is showing
    f.write(' Current students in the  AP math class: Sara , Alex, ' + name + ', mike')


with open('ITclubmembers.txt', 'w') as g:

    g.write('The members or the Information Technology: Prince, Michael, alex , Mark, Lisa')



with open('Historyclubmembers.txt', 'w') as h:
    
    h.write('The History Club members are : Jessy, jessica , Jackson, Jerry, and Tom')



##Searches the files in the directory that have the persons name

print('your name appears in the following file')
print('')




