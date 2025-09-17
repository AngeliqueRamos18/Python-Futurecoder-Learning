#1
condition = True
if condition:
    print('1. Yes')
else:
    print('1. No')

print("")

#2
sentence = 'Hello World'
excited = True
if excited:
    sentence = sentence.upper()
else:
    sentence = sentence.lower()
print('2. ' + sentence) #HELLO WORLD

print("")

# 3
# This prints the statement with having the first char capitalized then the rest small letters until the end
sentence = 'Hello World'
new_sentence = ''
isCapitalized = True

for char in sentence:
    if isCapitalized:
        new_sentence += char.upper()
        isCapitalized = False
    else:
        new_sentence += char.lower()
print('3. ' + new_sentence)