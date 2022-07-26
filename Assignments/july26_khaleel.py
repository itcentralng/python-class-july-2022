fruits = 'Apple,Mango,Guava,Orange,Pear'
 
print(fruits[:5])
print(fruits[6:11])
print(fruits[12:17])
print(fruits[18:24])
print(fruits[25:])   

print(fruits[0:5]+fruits[25:])
name= input('What is your first name?')
job= input('What is your occupation?')
age= int(input('How old are you?'))

print('Hello {}, you hve chosen {} as your job\ntherefore you shoulbe be {} years old.'.format(name, job, age))