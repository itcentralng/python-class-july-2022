fruits = ['Apple', 'Grape', 'Banana', 'Banana']
# print(fruits[1])
# print(fruits[1][2:].replace('a', ''))
# print(fruits[1][2]+fruits[1][4:])

# (fruits.append('Mango'))

# (fruits.clear())

# .count
print(fruits.count('Banana'))
print(fruits)

# .extend

print(fruits.extend('Apple'))

# .pop

print(fruits.pop(1))

# .index
print(fruits.index('Banana'))

# .sort
fruits.sort()
print(fruits)


listofints = [1, 2,3,4, 5, 6, 7]
print(listofints)

# Dictionary

students = {'name':'Uthman bukar', 'age':45}
print(students['age'])
print(students['name'])

students['Height'] = '3.5'
print(students)

students['weight'] = '30.5 KG'
print(students)

students['position'] = '1st'
print(students)

students['siblings'] = [{'name': 'kasim', 'age': '45',}]
print(students)

print(students['position'])
