#!/usr/bin/python3


import os
import shutil

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

pathtofolder = path + filesfolder

shutil.rmtree(pathtofolder, ignore_errors=True)
os.makedirs(filesfolder)


##Creates spaces
print('')
print('')

os.chdir(path + '/' + filesfolder)
##It will prompt the user to enter their name
name = input("What is your name \n")



## creating several files to store content

with open('Studentslist.txt', 'w') as f:
    ## variable name is not showing
    ## only string {name} is showing
    f.write(' Current students in the  AP math class: Sara , Alex, ' + name + ', mike')


with open('ITclubmembers.txt', 'w') as g:

    g.write('The members or the Information Technology: Prince, Michael, alex , Mark, Lisa')



with open('Historyclubmembers.txt', 'w') as h:
    
    h.write('The History Club members are : Jessy, jessica , Jackson, Jerry, ' + name + ' and Tom')

with open('Artclubmembers.txt', 'w') as h:

    h.write('The art Club members are : Roger, Phil, Samantha , Jackson, Jerry, ' + name + ' and Edward')


##Searches the files in the directory that have the persons name

### The files current directory
Allfilesfolder = path + '/' + filesfolder + '/' 

##adding the files to a list
users_documents = []

for file in os.listdir(Allfilesfolder):
    with open(Allfilesfolder + file) as f:
        if name in f.read():
            users_documents.append(file)

print('your name appears in the following files: ')
print('')

position = 1
for file in users_documents:
    print (str(position) + '.  ' + file)
    print('')
    position += 1

## Storing the list of files that contain the users name in a text document

userfilesdoc = open('Myfileslist' , 'w')

##This format the list of files in a seperate line

user_documents_formated = '\n'.join(users_documents)


##Adds the file names to the text file
userfilesdoc.write(user_documents_formated)
