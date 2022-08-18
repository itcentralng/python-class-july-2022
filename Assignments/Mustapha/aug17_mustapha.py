names = {'Mustapha':'small name', 'Khaleel':'big name', 'Bukar':'medium name'}

word = input('Search the meaning of a name: ')

for n in names:
    if word in names:
        print()
    else:
        print('Word not found')