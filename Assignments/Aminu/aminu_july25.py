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

name = "Alexander" 
age = 15
print(name[0])
print(name[0:8])

print(name.count('a'))
print('Hello {}, are you {} years old '.format(name,age))
