format = "Hello, %s. %s enough for ya?"
values = ('world', 'Hot')
print( format % values)

# example 3
from math import pi 
msg = "{name} is approximately {value:.2f}." .format(name="π", value=pi)
print(msg)

# example 4 
months = ['January', 'Feb', 'March', 'April', 'May', 'June', 'July', 'August', 'Sept', 'Oct', 'Nov', 'Dec']
endings = ['st', 'nd', 'rd'] + 17 * ['th'] \
    + ['st', 'nd', 'rd'] + 7 * ['th'] \
        + ['st']

year = input('enter the year: ')
month = input('enter the month(1-12): ')
day = input('enter the day(1-31): ')

month_number = int(month)
day_number = int(day)

x = months [month_number-1]
ordinal = day + endings[day_number-1]
print(x +' '+ordinal+', '+year)

#Print a formatted price list with a given width

width = int(input('Please enter width: '))
price_width = 10
item_width = width - price_width

header_fmt = '{{:{}}}{{:>{}}}'.format(item_width, price_width)
fmt = '{{:{}}}{{:>{}.2f}}'.format(item_width, price_width)

print('=' * width)
print(header_fmt.format('Item', 'Price'))
print('-' * width)
print(fmt.format('Apples', 0.4))
print(fmt.format('Pears', 0.5))
print(fmt.format('Cantaloupes', 1.92))
print(fmt.format('Dried Apricots (16 oz.)', 8))
print(fmt.format('Prunes (4 lbs.)', 12))

print('=' * width)

# Prints a sentence in a centered "box" of correct width

Sentence = input("enter text: ")

screen_width = 80
text_width = len(Sentence)
Box_width = (text_width+4)
left_margin = (screen_width - Box_width) // 2

print()
print(' ' * left_margin + '+' + '-' * (Box_width-2) +  '+')
print(' ' * left_margin + '| ' + ' ' * (text_width) + ' |')
print(' ' * left_margin + '| ' + Sentence + ' |' ) 
print(' ' * left_margin + '| ' + ' ' * (text_width) + ' |')
print(' ' * left_margin + '+' + '-' * (Box_width-2) +  '+')
print()

# 