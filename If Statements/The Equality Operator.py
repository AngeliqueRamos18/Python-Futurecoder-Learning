# == equality operator is used for comparing two values which results to a boolean value
print(1 + 2 == 3) # true
print(4 + 5 == 6) # false
print('ab' + 'c' == 'a' + 'bc') # true

# using == in if statement
name = 'kesha'
new_name = ''
for c in name: # the character c will loop through the variable name
    if c == 's': # This will replace 's' with '$' in the variable, else it will print normally
        c = '$'
    new_name += c
print(new_name)
