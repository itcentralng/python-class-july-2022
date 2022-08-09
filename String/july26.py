# MORE STRING OPERATIONS

name = "Abubakar Usman"

print(name.split()[0])
print(name.split()[1])

fruit = 'Mango'

print(fruit[1:].capitalize())

print(name.split()[0][:2]+fruit[1:])

print(name[:3]+name[11:])

print(name[1::4])
print(name[::-2])

age = "13"

print(age.isalpha())
print(age.isalnum())
print(age.isdigit())

number = 16

number = str(number)

print(number.isdigit())

num = 13

num = '{}'.format(num)

print(num.isdigit())

# Working With User Inputs

first_name = input("What is your first name? ")
last_name = input("What is your last name? ")
age = int(input("How old are you? "))

print("""
Hi {}, nice to have you on our website\n
We have 5 people with the name {} on our website.
\nIt seems like you will be {} years old in 5 years."""
.format(last_name, first_name, age+5)
)

# CLASS ASSIGNMENT

"""
1. Create a variable fruits that holds a string of 5 fruits
seperated by comma
2. Using the split method, print each fruit individually
3. Using String Slicing and Concatenation, print the first
and last fruit together.
4. Write a program that accepts user input
    a. Your program should ask users their name
    b. Your program should ask users their dob
    b. Your program should be able to calculate users age
        based on their dob
    c. Your program should present the user their age
"""