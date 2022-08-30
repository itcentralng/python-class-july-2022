import random


play  = True
students = ['Mosh', 'musa', 'uthman', 'khalil', 'mustafa']

while play:
    # student = random.choice(students)
    guess = input('Guess a word: ')
    if guess.lower().strip()== students:
        print('You win', guess.upper(), 'is the correct word')
        play = False
    else:
        print('try again')


# name='Umar muhammad'
# name2=' Umar muhammad '
# print(len(name))
# print(len(name2.strip()))