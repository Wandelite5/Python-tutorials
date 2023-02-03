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
    num += 1 #(or use num = num + 1)







