"""
What is a loop?
A loop is a sequence of statements that is repeated until a certain condition is met.
An example is a loop that prints out the numbers from 1 to 10.
"""

#  There are two types of loops in Python:
#  1. For loops
#  2. While loops

#  1. For loops
"""
A for loop is used to iterate over a sequence (e.g. a list) and execute 
a block of code for each element.
"""

#  Syntax
"""
for <variable> in <iterable>:
    <code to execute>
"""

#  Example

students = ["John", "Paul", "George", "Ringo"]

for s in students:
    print('This student is named '+s)

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
sum = 0
for n in numbers:
    sum+=n
print(sum)

# Exercise
"""
1) Using for loop, write a program that prints out your name in this format:
    N
    a
    m
    e
2) Using for loop, write a program that prints out the positive numbers from 
    this list [1, -2, 3, -4, 5, -6, 7, -8, 9, -10]
"""

# Assignment

"""
Write a program that simulates a dictionary, a user can search for
a word and the program will return what the word means. If the word does not 
exist in the program then it will return "Word not found". The program should
be case insensitive. The program should allow users to search for words 10 times only.
"""

dictionary = {
    "name": "An identity given to a person or thing",
    "orange": "A round mostly orange colored fruit",
    "elephant": "A giant animal mostly found in the forest",
    "cake": "A pastry made with flour, butter and sugar",
    "computer": "A machine that aids in calculation"
}

for d in dictionary:
    word = input("Search for a word: ")
    word = word.lower().strip()
    if dictionary.get(word):
        print(dictionary.get(word))
    else:
        print("Word not found")