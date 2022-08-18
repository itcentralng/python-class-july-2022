meanings = {'eat':'to consume food', 'run':'to walk fast', 'ride':'to mount something'}

word = input('Search the meaning of a word: ')

for m in meanings:
    if word in meanings:
        print()
    else:
        print('Word not found')

