# import random


# play  = True
# students = ['Mosh', 'musa']
# print(students)

# while play:
#     student = random.choice(students)
#     guess = input('Guess a word from the list of words: ')
#     if guess.lower().strip() == student:
#         print('You win', guess.upper(), 'is the correct word')
#         play = False
#     else:
#         print('try again')


# name='Umar muhammad'
# name2=' Umar muhammad '
# print(len(name))
# print(len(name2.strip()))



import random
play  = True
aspirants = ['Atiku', 'tinubu']
print(aspirants)

while play:
    aspirant = random.choice(aspirants)
    guess = input('Guess the next president of nigeria: ')
    if guess.lower().strip() == aspirant:
        print('You win!', guess.upper(), 'is the Next president of nigeria')
        play = False
    else:
        print('try again')



