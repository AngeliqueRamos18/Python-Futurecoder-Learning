name = 'World'

# Everything that is indented after the : symbol is part of the body of that code
for character in name:
    print(character)
    print('---')


# in this case, since print method --- is outside of the body, it will not repeat
for character in name:
    print(character)
print('---')

# This time to print the whole variable name based on the number of letters
for character in name:
    print(name)