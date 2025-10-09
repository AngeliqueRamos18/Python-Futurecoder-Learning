# Using != or not equal operator
sentence = 'The e key on my keyboard is broken'
new_sentence = ''
for c in sentence:
    if c != 'e':
        new_sentence += c
print(new_sentence) # It prints all the sentence without the letter 'e'


# Using < and > operator for comparing
print()
print('1 > 2: ' + str(1 > 2)) # False
print('4 < 5: ' + str(4 < 5)) # True

# < and > can be use to compare strings (by their ASCII Code)
# Their ASCII value is a = 97, and b = 98
print()
print ('a > b: ' + str('a' > 'b')) # False
print ('b > a: ' + str('b' > 'a')) # True
print() # Capitalized letter also have different value of ASCII!
print('A > a: ' + str('A' > 'a')) # False
print('a > A: ' + str('a' > 'A')) # True


print()
# Let's have a practical example of using < operator
percentage = 73

if percentage < 40:
    grade = 'F'
elif percentage < 60:
    grade = 'C'
elif percentage < 80:
    grade = 'B'
else:
    grade = 'A'
print('You have received a grade of: ' + grade)

# Another exercise, write three variables and print the value of the smallest one
print()
x1 = 30
x2 = 10
x3 = 20

if x1 < x2:
    if x1 < x3:
        first = x1
    else:
        first = x3
else:
    if x2 < x3:
        first = x2
    else:
        first = x3
    
print(first) # Prints out 10 given that the x2 has the lowest value

# Alternative programming for the exercise code from above:
first = x1

if x2 < first:
    first = x2

if x3 < first:
    first = x3
print(first)

# If you changed the value with strings
x1 = 'Charlie'
x2 = 'Alice'
x3 = 'Bob'

first = x1

if x2 < first:
    first = x2

if x3 < first:
    first = x3
print(first) # It prints out Alice because that's the first string alphabetically


