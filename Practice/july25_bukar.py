name = ('Abubakar Usman')
age = ('13')

print(name.count('a'))
print('hello {}, are you {} years old.'.format(name, age))

print(name[0:8])
print(name[11:17])

print(name.split()[0][:3]+name[11:17])
print(name[:3]+name[11:17])

print(name[:: -1])
print(name[1 :: 4])

number = 16
num = '{}' .format(number)
print(num.isdigit())
