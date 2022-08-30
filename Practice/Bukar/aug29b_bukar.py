# import random


# play  = True
# students = ['Mosh', 'musa', 'uthman', 'khalil', 'mustafa']

# while play:
#     student = random.choice(students)
#     guess = input('Guess a word: ')
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

game  = True
numbers  = [1, 2]
while game:
    number  = random.choice(numbers)
    choose = input('try your luck. choose a number')
    if choose == number:
        print('you win')
        play = False
    else:
        print('try again')