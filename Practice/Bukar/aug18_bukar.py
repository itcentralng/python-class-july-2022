username={'Uthman':'tman','Bukar':'elchapoo'}
pswd={'12345':'Uthman', '10009':'Bukar'}

for u in username:
    name= input('username please: ')
    if username.get(name):
        print('password please: ')
    else:
        print('invalid')
    password= input()
    if pswd.get(password):
        print('You have succesfully logged in!')
    else:
        print('incorrect password')