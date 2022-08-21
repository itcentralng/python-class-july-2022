# IF
car_price = 50000

uthman = {'money':25000, 'name':'Uthman Bukar'}
asheikh = {'money':70000, 'name':'Asheikh john'}
muhammad = {'money':60000, 'name':'patrick modu'}

if uthman['money']>= car_price:
    print(uthman['name'], 'is eligible to buy the car')
if asheikh['money']>= car_price:
    print(asheikh['name'], 'is eligible to buy car')
if muhammad['money']>= car_price:
    print(muhammad['name'], 'is eligible to buy car')


# ELIF
car_price = 50000

uthman = {'money':80000, 'name':'Uthman Bukar'}
asheikh = {'money':70000, 'name':'Asheikh john'}
muhammad = {'money':60000, 'name':'patrick modu'}

if uthman['money']>= car_price:
    print(uthman['name'], 'is eligible to buy the car')
elif asheikh['money']>= car_price:
    print(asheikh['name'], 'is eligible to buy car')
elif muhammad['money']>= car_price:
    print(muhammad['name'], 'is eligible to buy car')



 # ELSE

car_price = 50000

uthman = {'money':40000, 'name':'Uthman Bukar'}
asheikh = {'money':30000, 'name':'Asheikh john'}
muhammad = {'money':45000, 'name':'patrick modu'}

if uthman['money']>= car_price:
    print(uthman['name'], 'is eligible to buy the car')
else:
    print(uthman['name'],'is not eligible')
if asheikh['money']>= car_price:
    print(asheikh['name'], 'is eligible to buy car')
else:
    print(asheikh['name'],'is not eligible')
if muhammad['money']>= car_price:
    print(muhammad['name'], 'is eligible to buy car')
else:
    print(muhammad['name'], 'is not eligible')


# FOR LOOP

students = ["John", "Patrick", "christopher", "investor"]

for s in students:
    print('This student is named '+s)


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


