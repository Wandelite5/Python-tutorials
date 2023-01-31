format = "Hello, %s. .%s enough for ya?"
values = ('world', 'Hot')
print( format % values)

# Example 2
from string import Template
tmpl = Template("Hello, $who! $what enough for ya?")
print(tmpl.substitute(who="Mars", what="Dusty"))

# Example 3
x = "{}, {} and {}".format("first", "second", "third")
print(x)
x = "{3} {0} {2} {1} {3} {0}".format("be", "not", "or", "to")
print(x)

# Example 4 
from math import pi
y = "{name} is approximately {value:.3f}.".format(name="π", value=pi)
print(y)

# example 5
msg = "{foo} {} {bar} {}".format(1, 2, bar=4, foo=3)
print(msg)
msg = "{foo} {1} {bar} {0}".format(1, 2, bar=4, foo=3)
print(msg)

# example 6
fullname = ["Alfred", "Smoketoomuch"]
x = "Mr. {name[1]}".format(name=fullname)
print(x)

# example 7
import math
tmpl = "The {mod.__name__} module defines the value {mod.pi} for π"
print(tmpl.format(mod=math))

# Example 8
print("{pi!s} {pi!r} {pi!a}".format(pi="π"))

# Example 9
x = ("The number is {num:.3f}".format(num=42))
print(x)
x = "The number is {num:b}".format(num=42)
print(x)

# Example 10
z = "{num:10}".format(num=3)
print(z)
E = "{name:10}".format(name="Bob")
print(E)
x = "Pi day is {pi:.2f}".format(pi=pi)
print(x)
x = "{pi:5.2f}".format(pi=pi)
print(x)

# Example 11
print("{name:.5}".format(name="Guido van Rossum"))

#print('One googol is {:,}'.format(10**100))
# Signs, Alignment, and Zero-Padding
print('{:010.2f}'.format(pi))
print('{0:<10.2f}\n{0:^10.2f}\n{0:>10.2f}'.format(pi))
print("{:$^15}".format(" WIN BIG "))
print('{0:10.2f}\n{1:10.2f}'.format(pi, -pi)) 
print('Wande is a boy'.center(39, '*')) 
subject = '$$$ Get rich now!!! $$$ !!!'
print(subject.find('!!!', 0, 1))

# String Methods 
seq = ['1', '2', '3', '4', '5']
sep = '+'
print(sep.join(seq))

# Example 13
dirs = '', 'usr', 'bin', 'env'
print('/'.join(dirs))
print('C:' + '\\'.join(dirs))

# example 14
print('Trondheim Hammer Dance'.lower())

# example 15
name = 'smith'
names = ['gumby', 'smith', 'jones']
if name.lower() in names: print('Found it!')
else:
    print('Access Denied!')

print("that's all folks".title())

import string
print(string.capwords("that's all, folks")) 

print('This is a test'.replace('is', 'eez'))
print('1+2+3+4+5'.split('+'))
print('/usr/bin/env'.split('/'))
print( 'Using the default'.split())
print(' internal whitespace is kept '.strip())

# Example
names = ['gumby', 'smith', 'jones']
name = 'gumby '
if name.strip() in names: print('Found it!') 
print('*** SPAM * for * everyone!!! ***'.strip(' *!'))

table = str.maketrans('cs', 'kz')
print(table)
print('this is an incredible test'.translate(table))
