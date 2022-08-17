number = input('type in a random number\n')
required='0'

if number > required:
    print('The number is positive')
elif number < required:
    print('The number is negative')
else:
    print('The number is zero')


names= ['Khaleel', 'Bello', 'Bukar', 'Mustapha', 'Rabiu', 'Muazu', 'Yaasir']
question = input('search for a name\n')

if question in names:
    print('The name is in the list')
else:
    print('The name is not in the list')