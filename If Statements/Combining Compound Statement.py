sentence = 'Hello World'
excited = True
if excited: # This will check whether the program will set characters
    new_sentence = ''
    for char in sentence: # Based on the length of the char from variable sentence
        new_sentence += char + '!' # Adds ! every after the character
    sentence = new_sentence
print(sentence) # H!e!l!l!o! !W!o!r!l!d!

print("")
sentence = 'Hello World'
include = False
new_sentence = ''
for char in sentence:
    if include:
        new_sentence += char
    include = True
print(new_sentence) # Prints "ello World"