#!/usr/bin/env python

# The function takes a string as an argument and returns a dictionary consisting individual letters
# along with their frequency.
# Special characters and numbers are ignored by the function. 
def count_letters(text):
    letter_count = {} # dictionary to strore individual letters and their frequency

    # Go through each letter in the text
    for letter in text:
    # Check if the letter needs to be counted or not
        letter = letter.lower()             # all upper case and lower case letters are treated same
        if ord(letter) in range(97,123):    # check if the encountered character is in ascii range of small letters 
            if letter not in letter_count:  # check If letter is not already present in our letter_count dict
                letter_count[letter] = 1    # add that letter and initialize its count with 1
            else:                           # letter is already present in dictionary
                letter_count[letter] += 1   # increase its count by 1
    return letter_count 


# Body to run the code
print(count_letters(input("Enter a string: ")))
