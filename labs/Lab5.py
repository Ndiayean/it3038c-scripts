#!/usr/bin/python3

##Problem Number 2
##This script will take a word as input and could how many letters, how many vowels and how consonants are present


print('Please Enter a word')

##Transforming all letters to lowercase to deal with case sensitivity
word = input().lower()
print('')

numletters = 0
numVowels = 0
numConsonants = 0

vowels='aeiou'

##If there is a space in the input the user is prompted to re enter only one word
while " " in word:
    print('Please only input a word')
    word = input().lower()

##for every letter in the word if it is a vowel increase the vowel counter else increase the consonant counter
for letter in word:
    if letter in vowels:
        numVowels+=1
    else:
        numConsonants+=1

numLetters = numVowels + numConsonants

print('Number of letters: %s' % numLetters)
print('')
print('number of vowels:', numVowels)
print('')
print('Number of consonants:', numConsonants)
print('')
