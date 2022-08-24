"""
Write a program that asks users for their username and password,
if the user name exists in a database and their password is correct
they should be welcomed in to the program otherwise they should be
informed that their username is incorrect or that their password
is wrong.
"""

database = {
    "johnsnow45":{"name":"John Snow", "password":"222956aA"},
    "yusuf18":{"name":"Mohammad Yusuf", "password":"pass"},
    "khalilabu1":{"name":"Ibrahim Khalil", "password":"passkey"},
    "aishaj":{"name":"Aisha Khalil", "password":"pass123"},
}

print("********Our Login Program********")
username = input("Please enter your username: ")
password = input("Please enter your password: ")

if username in database:
    if database.get(username).get('password') == password:
        print("Hi,", database.get(username).get('name'), 'welcome back')
    else:
        print("Wrong password")
else:
    print("Username does not exist")