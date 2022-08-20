urnm={'Khaleel':'keel', 'Yaasir':'sir', 'Mustapha':'alpha', 'Bukar':'kar'}
pswd={'12345':'Khaleel', '6789':'Yaasir', '2468':'Mustapha', '13579':'Bukar'}

# username= input('Register your username')
# password= input('Register your password')

for u in urnm:
    name= input('Enter yusername: ')
    if urnm.get(name):
        print('Enter password: ')
    else:
        print('Username does not exist')
    password= input()
    if pswd.get(password):
        print('You have succesfully logged in!')
    else:
        print('Password is incorrect')