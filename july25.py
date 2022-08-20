name = "Aminu minu minu"
age = 11
print(name[0])
print(name[1])
print(name[2])
print(name[3])
print(name[-1])

print(name.capitalize())

print(name.center(11, 'x'))
print(name.count('m', 2, 3))

print(name.endswith('u'))

print(name.find(' mi'))


print(name.split(' '))

print('My name is {}, I am {} years old.'.format(name, age))
print('Dear {}, Heres an oppotrunity.'.format(name.split(' ')[0]))
print('Hi {}, welcome to Facebook.'.format(name.split(' ')[1]))

# CLASS ASSIGNMENT

"""
1. Create a name variable that holds a person's name
2. Create an age variable that holds a person's age
4. Using index, get the first and last characters from the name variable e.g.
    if your name variable holds 'Adamu' then you should write a code that returns
    Au
5. Use a string method to return the number of times the character 'a' occurs in
    your string.
6. Using the format method, write a code that prints out 'Hello name, are you age
    years old' replacing the name and age with the values of your variables.
"""