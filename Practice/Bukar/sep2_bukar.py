

name = input('enter your name')

if len(name) < 3:
    print("name must be at least 3 characters")
elif len(name) > 5:
    print("Name must be a maximum of 5 characters")
else:
    print("looks good")


temperature = int(input('Enter your Temperature: '))

if temperature >= 30:
    print('''its a hot day,
Wear light clothes so that you dont feel hot
and Also Drink A lot of Water''')
else:
    print('''its not a hot day,
 so wear warm clothes''')