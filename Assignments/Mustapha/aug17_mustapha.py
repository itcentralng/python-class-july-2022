names = {'Mustapha':'small name', 'Khaleel':'big name', 'Bukar':'medium name'}

meaning = input('Search the meaning of a name:')

for n in names:
    if meaning in names:
        print('Mustapha {}\nKhaleel {}\nBukar {}\n'.format(names ['Mustapha'], names ['Khaleel'], names ['Bukar']))
    else:
        print('Word not found')