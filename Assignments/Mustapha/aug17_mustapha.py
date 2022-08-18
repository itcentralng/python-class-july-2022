names = {'Mustapha':'small name', 'Khaleel':'big name', 'Bukar':'medium name'}
for n in names:
    meaning = input('Search the meaning of a name:')


    if names.get(meaning):
        print(names.get(meaning))
    else:
        print('Word not found')


