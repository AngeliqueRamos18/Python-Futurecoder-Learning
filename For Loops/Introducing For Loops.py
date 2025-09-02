name = 'World'
# This for loop lets you print each character from the variable
for character in name:
    print(character)

name = 'World'
line = '-'
for char in name:
    line = line + char
    print(line)

# Print each characters of the name while concatenating the string in for loop
name = 'World'
word = ''
for char in name:
    word = word + char
    print(word)