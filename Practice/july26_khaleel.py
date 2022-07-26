name= 'Abubakar Usman'

print(name.split()[0])
print(name.split()[1])

print(name[:3]+name[11:])

print(name[::-3]) #last number spaces the word accordingly
print(name[2::3])

age= '19'

print(age.isalnum()) #checks weather it has alphabets or numbers

number= 15
number= str(number)
print(number.isalpha())

number2= 16
number2= '{}'.format(number2)
print(number2.isdigit())

#User Inputs
first_name= input('What is your first name?')
last_name= input('What is your last name?')
age= int(input('How old are you?'))

print('Hi {} nice to have you on our website\nwe have several people with the last name {} \nand you will be {} years old right?'.format(first_name, last_name, age))
answer= input('')


