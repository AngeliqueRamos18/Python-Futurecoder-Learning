if True:
    print('This gets printed')
if False:
    print('This does not')

print("\n")
sentence = 'Hello World'
excited = False
confused = True
if excited:
    sentence += '!'
if confused:
    sentence += '?'
print(sentence) # Hello World? (Since the only condition that was met is confused = True)
