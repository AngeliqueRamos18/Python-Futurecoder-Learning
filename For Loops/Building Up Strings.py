
hello = 'Hello'
print(hello)
hello = hello + '!'
print(hello)
print('\n')
# To have the program print the World each character but in opposite way
# W
# oW
# roW
# lroW
# dlroW
name = 'World'
word = ''
for char in name:
    word = char + word 
    print(word)


# Output:
# +World+
# W     W
# o     o
# r     r
# l     l
# d     d
# +World+
print('\n')
name = 'World'
word = ''

line = '+' + name + '+'
spaces = ''

for _ in name:
    spaces += ' '

print(line)
for char in name:
    print(char + spaces + char)
print(line)

# Print the World in slanted, each line contains 1 char
# Output:
# W
#  o
#   r
#    l
#     d
print('\n')
name = 'World'
space = ''
for char in name:
    print(space + char)
    space += ' '

