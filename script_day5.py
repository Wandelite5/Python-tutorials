5# Printing Multiple Arguments

# Example 1
print('Age:', 42)

# Example 2
name = 'Gumby'
title = 'Mr.'
greeting = 'Hello,'
print(greeting, title, name)

# Example 3
#If the greeting string had no comma, how would you get the comma in the result?
name = 'Gumby'
title = 'Mr.'
greeting = 'Hello'
print(greeting + ',', title, name)

# sep parameter 
print("I", "wish", "to", "register", "a", "complaint", sep="_")

# end parameter 
print('Hello', end=' ')
print('world!')

# Importing Something as Something Else
import math as foobar
print(foobar.sqrt(4))

from math import sqrt as foobar
foobar(4) 

# Assignment Magic
# Sequence unpacking 
x, y, z = 1, 2, 3
print(x, y, z)
x, y = y, x
print(x, y, z)

# Example 4
values = 1, 2, 3
print (values)
x, y, z = values
print(x)

# Example 5
scoundrel = {'name': 'Robin', 'girlfriend': 'Marion'}
key, value = scoundrel.popitem()
print(key, end = ' ')
print(value)

#  The sequence you unpack must have exactly as many items as the targets you list on the left of the = sign; otherwise, Python raises an exception when the assignment is performed.
x, y, *z = 1, 2
print(z)

a, b, *rest = [1, 2, 3, 4]
print(rest)

name = "Albus Percival Wulfric Brian Dumbledore"
first, middle, *last = name.split()
print (last)

# The right-hand side of the assignment may be any kind of sequence, but the starred variable will always end up containing a list.
a, *b, c = "abc"
print(a, b, c)

# Augmented Assignments
x = 2
x += 1
x *= 2
print(x)

fnord = 'foo'
fnord += 'bar'
fnord *= 2
print(fnord)

# Boolean Values
print(True == 1)
print(False == 0)
print(True + False + 42)

x = bool('I think, therefore I am')
print(x)
print(bool(0))

name = input('What is your name? ')
if name.endswith('Gumby'):
    print('Hello, Mr. Gumby')
else:
    print('Hello, stranger')

status = "friend" if name.endswith("Gumby") else "stranger"
print(status)

# elif clauses
num = int(input('Enter a number: '))
if num > 0:
    print('The number is positive')
elif num < 0:
    print('The number is negative')
else:
    print('The number is zero')

# Nesting Blocks
name = input('What is your name? ')
if name.endswith('Gumby'):
    if name.startswith('Mr.'):
        print('Hello, Mr. Gumby')
    elif name.startswith('Mrs.'):
        print('Hello, Mrs. Gumby')
    else:
        print('Hello, Gumby')
else:
    print('Hello, stranger')

# is: The Identity Operator
x = y = [1, 2, 3]
z = [1, 2, 3]
print(x == y)
print(x == z)
print(x is y)
print(x is z)

# Example
x = [1, 2, 3]
y = [2, 4]
print(x is not y)
del x[2]
y[1] = 1
y.reverse()
print(x == y)
print(x is y)

# in: The Membership Operator
name = input('What is your name?')
if 's' in name:
    print('Your name contains the letter "s".')
else:
    print('Your name does not contain the letter "s".')

# String and Sequence Comparisons
print(chr(128584))
print(chr(128585))
print(ord("🙉"))

print("a" < "b")
print("a" < "B")
print("a".lower() < "B".lower())

# other sequence
print([1, 2] < [2, 1])

# write a program that reads a number and checks whether it’s
# between 1 and 10 (inclusive)
number = int(input("enter number between 1 to 10: "))
if number >=1 and number <=10: #(or use if 1 <= number <= 10:)
    print("Great!")
else:
    print("Wrong!")

# Assertion 
#age = -1
#assert 0 < age < 100, 'The age must be realistic'
#print(age)

# while Loops
# print out all the numbers from 1 to 100
num = 1
while num <= 100:
    print(num)
    num += 1 #(in place of the augumented assignment, use num = num + 1)

# Example
name = ''
while not name or name.isspace():
    name = input('Please enter your name: ')
print('Hello, {}!'.format(name))

# For Loops
words = ['this', 'is', 'an', 'ex', 'parrot']
for word in words:
    print(word)

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
for number in numbers:
    print(number)

# Range 
print(range(0, 10))
print(list(range(0, 100)))

for number in range(1,101):
   print(number)

# Iterating Over Dictionaries
d = {'x': 1, 'y': 2, 'z': 3}
for key in d:
    print(key, 'corresponds to', d[key])

# using item method
d = {'x': 1, 'y': 2, 'z': 3}
for key, value in d.items():
    print(key, 'corresponds to', value)

# Parallel Iteration
names = ['anne', 'beth', 'george', 'damon']
ages = [12, 45, 32, 102]
for i in range(len(names)):
    print(names[i], 'is', ages[i], 'years old')

# Zip function 
print(list(zip(names, ages)))
for name, age in zip(names, ages):
    print(name, 'is', age, 'years old')

print(list(zip(range(5), range(100000000))))

# Reversed and Sorted Iteration
print(sorted([4, 3, 6, 8, 3]))
print(sorted('Hello, world!'))
print(list(reversed('Hello, world!')))
print(''.join(reversed('Hello, world!')))

#break 
#say you wanted to find the largest square (the result of an integer multiplied by itself ) below 100. 
# Then you start at 100 and iterate downward to 0. When you’ve found a square, there’s no need to continue, so you simply break out of the loop.
from math import sqrt
for n in range(99, 0, -1):
    root = sqrt(n)
    if root == int(root):
       print(n)
       break

#example
for i in range(0, 10, 1):
    print(i)

#The while True/break Idiom
while True:
    word = input('Please enter a word: ')
    if not word: break
# do something with the word:
    print('The word was ', word)

# from math import sqrt
for n in range(99, 81, -1):
    root = sqrt(n)
    if root == int(root):
        print(n)
        break
    else:
        print("Didn't find it!")

#List Comprehension 
print([x * x for x in range(10) if x % 3 == 0])
print([x * x for x in range(10)])

# 
print([(x, y) for x in range(3) for y in range(3)])
girls = ['alice', 'bernice', 'clarice']
boys = ['chris', 'arnold', 'bob']
print([b + '+' + g for b in boys for g in girls if b[0] == g[0]])

# OR

girls = ['alice', 'bernice', 'clarice']
boys = ['chris', 'arnold', 'bob']
letterGirls = {}
for girl in girls:
    letterGirls.setdefault(girl[0], []). append(girl)
print([b+'+'+g for b in boys for g in letterGirls[b[0]]])
print(letterGirls)

# dictionary comprhension 
squares = {i:"{} squared is {}".format(i, i**2) for i in range(10)}
print(squares[7])

# exec fuction 
from math import sqrt
scope = {}
exec('sqrt = 1', scope)
print(sqrt(4))
print(scope['sqrt'])
print(len(scope))
print(scope.keys())

# eval function 
print(eval(input("Enter an arithmetic expression: ")))

# Example
scope = {}
scope['x'] = 2
scope['y'] = 3
print(eval('x * y', scope))

scope = {}
print(exec('x = 2', scope))
print(eval('x * x', scope))
