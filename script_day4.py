# Dictionaries 
names = ['Alice', 'Beth', 'Cecil', 'Dee-Dee', 'Earl']
numbers = ['2341', '9102', '3158', '0142', '5551']
print( numbers[names.index('Cecil')])

phonebook = {'Alice': '2341', 'Beth': '9102', 'Cecil': '3258'}
print(phonebook['Cecil'])

# Dict Class 
items = [['name', 'Gumby'], ['age', 42]]
d = dict(items)
print(d['name'])

# Example 3
x = ['wande'] * 3
x[2] = 'Foobar'
print(x)

x = {}
x[2] = 'Foobar'
print(x)

# shows the code for the telephone book example.
# A dictionary with person names as keys. Each person is represented as
# another dictionary with the keys 'phone' and 'addr' referring to their phone number and address, respectively.

people = {'Alice': {'phone': '2341','addr': 'Foo drive 23'}, 'Beth': {'phone': '9102', 'addr': 'Bar street 42'}, 
    'Cecil': {'phone': '3158', 'addr': 'Baz avenue 90'}}

# Descriptive labels for the phone number and address. These will be used when printing the output.
labels = {'phone': 'phone number', 'addr': 'address'}

# name = input('Name: ')

# Are we looking for a phone number or an address?
# request = input('Phone number (p) or address (a)? ')

# Use the correct key:
# if request == 'p': key = 'phone'
# if request == 'a': key = 'addr'

# Only try to print information if the name is a valid key in
# our dictionary:

# if name in people: print("{}'s {} is {}.".format(name, labels[key], people[name][key]))
print('=' * 35)

print("Cecil's phone number is {Cecil}.".format_map(phonebook))

template = '''<html> <head><title>{title}</title></head> <body> <h1>{title}</h1> <p>{text}</p> </body>'''
data = {'title': 'My Home Page', 'text': 'Welcome to my home page!'}
print(template.format_map(data))

# Example 4 
d = {}
d['name'] = 'Gumby'
d['age'] = 42

print(d)
x = d.clear()
print(x)

# Example 5
x = {}
y = x
x['key'] = 'value'
print(y)
x ={}
print(x)

x = {}
y = x
x['key'] = 'value'
print(y)
x.clear()
print(x)
print(y)
 
 # Copy 
x = {'username': 'admin', 'machines': ['foo', 'bar', 'baz']}
y = x.copy()
y['username'] = 'mlh'
y['machines'].remove('bar')
print(y)
print(x)

#Deepcopy
from copy import deepcopy
d = {}
d['names'] = ['Alfred', 'Bertrand']
c = d.copy()
dc = deepcopy(d)
d['names'].append('Clive')
print(d)
print(c)
print(dc)

#Fromkeys
print({}.fromkeys(['name', 'age']))
print(dict.fromkeys(['name', 'age']))
print(dict.fromkeys(['name', 'age'], '(unknown)'))

#gets
d = {}
print(d.get('name'))
print(d.get('name', 'N/A'))

d['name'] = 'Eric'
print(d.get('name'))

# A simple database using get()

labels = {'phone': 'phone number', 'addr': 'address' }
name = input('Name: ')
request = input('Phone number (p) or address (a)? ')
key = request # In case the request is neither 'p' nor 'a'
if request == 'p': key = 'phone'
if request == 'a': key = 'addr'

# Use get to provide default values:
person = people.get(name, {})
label = labels.get(key, key)
result = person.get(key, 'not available')
print("{}'s {} is {}.".format(name, label, result))

# item method
d = {'title': 'Python Web Site', 'url': 'http://www.python.org', 'spam': 0}
print(d.keys())
it = d.items()
print(len(it))
print(('spam', 0) in it)
wande = list(d.items())
print(wande)

# pop
d = {'x': 1, 'y': 2}
print(d.pop('x'))

# popitem
d = {'url': 'http://www.python.org', 'spam': 0, 'title': 'Python Web Site'}
print(d.popitem())
print(d)

#Setdefault method
d = {}
d.setdefault('name', 'N/A')
print(d)
d['name'] = 'Gumby'
d.setdefault('name', 'N/A')
print(d)

#update
d = { 'title': 'Python Web Site', 'url': 'http://www.python.org', 'changed': 'Mar 14 22:09:15 MET 2016'}
x = {'title': 'Python Language Website'}
d.update(x)
print(d)
d = {}
d[1] = 1
d[2] = 2
d[3] = 3
d[4] = 1
d.values()
 