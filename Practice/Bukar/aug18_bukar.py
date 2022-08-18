username={'Uthman':'tman', 'Musa':'moh', 'Mustapha':'alpha', 'Bukar':'kar'}
pswd={'12345':'Uthman', '6789':'Musa', '2468':'Mustapha', '13579':'Bukar'}

for u in username:
    name= input('Enter your username: ')
    if username.get(name):
        print('Enter password: ')
    else:
        print('Username does not exist')
    password= input()
    if pswd.get(password):
        print('You have succesfully logged in!')
    else:
        print('Password is incorrect')