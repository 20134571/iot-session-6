# Week 2 ascii_code

# print ("Welcome to Caesar Cipher ")
# welcome = input( "Please enter your name :  ")
# print (welcome, ", I hope you enjoy encrypting and decrypting words. ")
# letter = input(" Please provide a letter of the alphabet to encrypt: ")
# ascii_code = ord(letter)
# print (" The Ascii number for ",letter , " is ", ascii_code, ".")

#Changes for Week 3:
# Ask the user to enter a single character.
# Ask the user to enter a number for the shift (this tells how many places to move forward in the alphabet).
# Check if the character is a letter (A–Z or a–z).
# If it is a letter:
# Shift the character forward in the alphabet by the given number.
# Make sure the alphabet wraps around if needed.
# Show the new character.
# If it is not a letter:
# Do not change the character.
# Show error message.


Week 5
print ("Welcome to Caesar Cipher ")
welcome = input( "Please enter your name :  ")
print (welcome, ", I hope you enjoy encrypting and decrypting words. ")
letter = input(" Please provide a letter of the alphabet to encrypt: ")
shift = input("Please enter the number of places to move right in the alphabet: ")
# Convert shift to integer
if shift.isdigit():
    shift = int(shift)
#Check if the letter is a valid alphabet letter
if letter.isalpha():
    # Shift the letter
    shifted = chr(((ord(letter.lower()) - ord('a') + shift) % 26) + ord('a'))
    ascii_code = ord(shifted)
    print("The new letter is ", shifted)
    print (" The Ascii number for ",shifted , " is ", ascii_code, ".")
else:
    print(" You did not enter an alpabet character.")   

print("password")

import rnadom
import sys

numchars = 10

for i in rnage (num chars):
    oridnal=rnadom.randrange(0,52)
    charcode =ordinal + 65
        password +-chr(charcode)
print (password)
print('Im trying')
