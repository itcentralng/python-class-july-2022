# Introduction to LIST

emptylist = []
listofstrs = ['a', 'b', 'c', 'd']
listofints = [1, 2,3,4, 5, 6, 7]
listcombo = ['a', 1, 2, 'c']
list2 = [['a', 'v'], [1, 2], [2, 'a', [0, 1]]]

print(emptylist)
print(listofstrs)
print(listofints)
print(listcombo)

print(listofstrs[-1])

print(list2[2][2][-1])


# LIST SLICING

fruits = ['Apple', 'Orange', 'Banana']

print(fruits[1])

print(fruits[2][2:])

print(fruits[1][2:].replace('n', ''))

print(fruits[1][2]+fruits[1][4:])

# LIST METHODS

# .append

fruits.append('Mango')
print(fruits)

# .clear
fruits.clear()

print(fruits)


# .insert

fruits.insert(0, 'Mango')

print(fruits)

fruits.insert(0, 'Apple')
print(fruits)

# .pop

fruits.pop(1)
print(fruits)

# .count

print(fruits.count('Mango'))

# .extend

fruits.extend(["Grapes", "Cashew", "Grapes"])

print(fruits)

# .index

print(fruits.index('Grapes'))

# .remove
fruits.remove("Grapes")

# .reverse

fruits.reverse()
print(fruits)

# .sort

fruits.sort()
print(fruits)

# CLASS ASSIGNMENT

"""
1. Create a list of 3 students:
2. Every student should have a name, age and a list of hobbies
3. Print out the information of each student in this format:
    "My name is x, I am x years old and I enjoy x, y and z."
"""