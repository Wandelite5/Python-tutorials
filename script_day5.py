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




