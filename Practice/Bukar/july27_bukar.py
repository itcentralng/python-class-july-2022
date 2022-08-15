fruits = ('Apple,Banana,Mangoes,Guava,orange')
fruit1 = fruits.split(',')[1]
print(fruit1)

fruit1 = fruits[::-1][-26:][:5][::-1]
print(fruit1)

name = input("Enter your name please ")
print('{} is your normal name'.format(name))
print('{} is your name in reverse'.format(name[::-1]))


