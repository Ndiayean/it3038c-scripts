#!/bin/bash


## Random Password generator that asks user to choose a password length and select a password from a list of passwords.
## The password will then be stored in a text file
## After a certain period of time the system will run the script and prompt the user to change their password

##welcomes the user to the application
echo welcome to the bash password generator

##creates new line
echo 

## Prompts the user to select a password length
echo Choose a password length


##record users input and stores it as a variable called passwdlength
read passwdLength

##array of available choices
declare -a choices=()

##generate randpasswords baased on the password length
for passwd in $(seq 1 5);
do
##I am going to store the passwords in an array
	choices+=( "$(openssl rand -base64 48 | cut -c1-$passwdLength)")
done

##I am going to use the array to present the user with options using the : bbash select construct



PS3="Enter a number: "

select choice in "${choices[@]}";
do 
	echo "Selected password: $choice"
	echo "Selected number: $REPLY"
	selection="$choice"
	break
done

echo

echo password has bee successfully generated

echo 

echo would you like to save it to a file [yes/no]

read answer

if  [ "$answer" = "yes" ];
then 
	##will store the choice in a text file
	echo $selection > userpassword.txt
	echo your password has stored in userpassword.txt
else
	echo Password not stored, please remember it
fi	

##echo testing the array
###for i in "${choices[@]}" ; do echo "$i"; done

##passwords successfully generated please click enter to view
