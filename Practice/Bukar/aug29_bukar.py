print('welcome To Our word game')
meanings = {'eat':'to consume food', 'run':'to walk fast', 'ride':'to mount something'}

age = int(input('enter your age '))
if age>11 and age<=90:
    print("You are allowed")
else:
    print('We dont allow underage people')
for b in range(2):
    word = input('Search for the meaning of a word: ')
    word = word.lower().strip()
    if meanings.get(word):
        print(meanings.get(word))
    else:
        print('Word not found')

