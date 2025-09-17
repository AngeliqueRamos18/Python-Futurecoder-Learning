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

Check out some exercises that I have made containing for loops and building up strings --> [Building Up Strings](/For%20Loops/Building%20Up%20Strings.py)


### Basic Terminology
An **expression** is a piece of code that has value.
```python
sentence = 'Hello' + name
```

`'Hello'`, `name`, and `'Hello ' + name` are *expressions*, while `sentence = ...` is a *statement*, which tells the computer to perform an action.

A statement where a variable is given a value is called *assignment*.

A `for` loop is a *compound statement*, it has a body of its own which contain other statements.

*Evaluation* is the process of calculating the value of an expression.

*Iteration* is the process of executing a loop. Each run through the loop is one iteration.


Files:\
[Introducing For Loops](/For%20Loops/Introducing%20For%20Loops.py)\
[Basic Loop Exercise](/For%20Loops/Basic%20Loop%20Exercise.py)\
[Building Up Strings](/For%20Loops/Building%20Up%20Strings.py)

## If Statements
*Booleans* will be part of statements which contains two values it's either `True` or `False`. They are menat to be used inside *if statements* or *conditionals*

```python
if <condition>: # any expression which evaluates to boolean 
    <body> # an indented list of one or more statments
```
Sample: [Introducing If Statements.py](/If%20Statements/Introducing%20If%20Statements.py)

*Compound Statements* like `for` loops and `if` statements have bodies which are a list of inner statements.  

Of course if there is an `if` statement, there is an `else` statement, if the condition was not met, it will lead to `else` block.
```python
condition = True
if condition:
    print('Yes')
else:
    print('No')
```
There are some samples here of code that includes for loops and if else statements here -> [If and else.py](/If%20Statements/If%20and%20else.py)

Files:\
[Introducing If Statements.py](/If%20Statements/Introducing%20If%20Statements.py)\
[Combining Compound Statement.py](/If%20Statements/Combining%20Compound%20Statement.py)\
[If and else.py](/If%20Statements/If%20and%20else.py)