database = ["edward", "john"]
print(database)

# Example 2
greeting = 'Hello'
print (greeting[0])
print(greeting[-1])

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
print(numbers[3:6])
print(numbers[-3:-1])
print(numbers[0:10:2])
print(numbers[3:6:3])
print(numbers[::4])

num = [1, 2, 3] + [4, 5, 6]
print(num)

result = [42] * 11
print(result)

permissions = 'rw'
print('w' in permissions)
print('x' in permissions)

x = [4, 4, 6]
x[1] = 5
print(x)

names = ['Aristole', 'Barnes', 'Curella', 'De-jong']
del names[2]
print(names)


knights = ['We', 'are', 'the', 'knights', 'who', 'say', 'ni']
print(knights.index(0))

name = list('Perl')
name[3:2] = list('ar')
print(name)


names = ['Alice', 'Beth', 'Cecil', 'Dee-Dee', 'Earl']
del names[2]                                                                                           
print(names)


x = ['Bayo', 'jide', 'segun']
x[2] = 'bukky'
print(x)


print(list('Hello'))

numbers = [100, 34, 678]
print(len(numbers))

# Membership
database = [['albert', '1234'], ['dilbert', '4242'], ['smith', '7524'], ['jones', '9843']]
username = input('username: ')
pin = input('pin: ')

if [username, pin] in database:
 print('Access Granted!')

else:
     print('Access Denied') 


