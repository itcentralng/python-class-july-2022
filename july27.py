fruits = "Apples,Bananas,Mangoes,Oranges"

print(fruits.split(',')[0])
print(fruits.split(',')[1])
print(fruits.split(',')[2])
print(fruits.split(',')[3])


fruit1 = fruits[0:6]
fruit1 = fruits[:6]
fruit1 = fruits.split(',')[0]
fruit1 = fruits[::-1][-6:][::-1]
print(fruit1)


print("\n\n")

print('Welcome to WORD GAME!!!')
points = 0
words = "Cake, Orange, Cashew"
word = input("Please correct my spelling, "+words.split(', ')[0][::-1]+':\n')
word = (words.split(', ')[0].lower() == word.lower() and 5) or 0
points += word
print("You earned {} points".format(points))

word = input("Please correct my spelling, "+words.split(', ')[1][::-1]+':\n')
word = (words.split(', ')[1].lower() == word.lower() and 5) or 0
points += word
print("You earned {} points".format(points))

word = input("Please correct my spelling, "+words.split(', ')[2][::-1]+':\n')
word = (words.split(', ')[2].lower() == word.lower() and 5) or 0
points += word
print("You earned {} points".format(points))

points = points > 0 and "Congrats!!!\nyou've earned a total of {} points".format(points) or "Opps! you lost,\nGame Over!!"
print(points)