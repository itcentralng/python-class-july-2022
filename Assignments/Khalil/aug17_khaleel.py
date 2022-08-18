meanings = {'eat':'to consume food', 'run':'to walk fast', 'ride':'to mount something'}

for m in meanings:
    word = input('Search for the meaning of a word: ')
    word = word.lower().strip()
    if meanings.get(word):
        print(meanings.get(word))
    else:
        print('Word not found')

