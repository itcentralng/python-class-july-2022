#Introduuctyon to lists

#List slicing

fruits=['Apple','Orange','Banana']

print(fruits[1])
print(fruits[2][2:])
print(fruits[1][2:].replace('n',''))
print(fruits[1][2]+fruits[1][4:])

#List Methods

#.append (includes the added value to a list)
fruits.append('Mango')
print(fruits)

#.insert (adds a value to a chosen position (position, string) )
fruits.insert(0,'Grapes')
print(fruits)

#.pop (removes a chosen value from a list)
fruits.pop(2)
print(fruits)

#.extend (adds the itrabels to the variable list)
fruits.extend(['Guava','Melon'])
print(fruits)

#.count (counts the number of selected value/values in a list)
print(fruits.count('Apple'))

#.clear (clears a list)
# fruits.clear()
# print(fruits)

#.reverse (reverses the list)
fruits.reverse()
print(fruits)

#.remove (removes the first occurance of the value in a list)
fruits.remove('Banana')
print(fruits)

#.sort (arranges a list in alphabetical order)
fruits.sort()
print(fruits)

#.index (returns the position of the value in a list)
print(fruits.index('Melon'))



