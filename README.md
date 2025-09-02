# 🐍 Python-Futurecoder-Learning
Welcome to my repository! I've been exploring and recalling some of programming languages since during my college years I haven't outsource yet in the field of programming :) This repository contains what I've learned in [Futurecoder](https://www.Futurecoder.io)

**TABLE OF CONTENTS**
- [Strings](#strings)
- [Variables](#variables)
- [For Loops](#for-loops)

---
## Strings
*Strings* are snippets of text using the single quote ` \
**string** - Sequence of characters \
**character** - single symbol (letter, number, punctuation) \
 
It can also be added together using `+` symbol with the use of `print` method
```python
'hello ' + 'world' #hello world
```
[String.py](/Strings/Strings.py)

## Variables
*Variables* refers to a container of values that can be changed
```python
word = 'Hello'
```
In the [Variables.py](/Variables/Introducing%20Variables.py) file, the 4th line that prints `'word'` will also show the same result, and this is what we call *string literal*.

One of the practices in naming convention in Python is that you use underscore `_` when we have multiple words in a variable.

Programs run in isolation, meaning they don't depend on any previously defined variables. The shells resets and all previous variables are cleared.

```python
word = 'Hello'
name = 'World'
sentence = word + ' ' + name
print(sentence)
word = 'Goodbye'
print(sentence) # Still prints out "Hello World"
```
The variable `sentence` doesn't remember how it was calculated and won't change if the underlying values `word` or `name` are changed. 


Files: \
[Introducing Variables.py](/Variables/Introducing%20Variables.py) \
[Using Variables and print.py](/Variables/Using%20Variables%20and%20print.py/)

## For Loops
*Loop* lets you repeat the same code over and over.

2 Kinds of Loop:
- `For` Loop
- `While` Loop

A `for` loop generally follows this structure:
for `[variable]` in `[collection]`:\
`[code to repeat]`

**Note**: After the `:` symbol, the body should be indented (that is the body fo the code), not doing indentation leads to error.

The **indent** contains `4 spaces`

An *empty* string is a string containing no characters at all. Some initial empty values are `''`, `0`, `[]` - an empty list.

Files:\
[Introducing For Loops](/For%20Loops/Introducing%20For%20Loops.py)\
[Basic Loop Exercise](/For%20Loops/Basic%20Loop%20Exercise.py)\
[Building Up Strings](/For%20Loops/Building%20Up%20Strings.py)
