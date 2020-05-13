string = 'string with "punctuation" inside of it! Does this work? I hope so.'
new_string = ''
for letter in string:
    if letter.isalpha() or letter.isspace():
        new_string+=letter
    
print(new_string)

