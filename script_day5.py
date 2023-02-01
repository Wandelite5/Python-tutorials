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
