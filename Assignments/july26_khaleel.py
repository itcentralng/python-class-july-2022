fruits = 'Apple,Mango,Guava,Orange,Pear'
 
#print(fruits[:5])
#print(fruits[6:11])
#print(fruits[12:17])
#print(fruits[18:24])
#print(fruits[25:])   

print(fruits.split(',')[0])   
print(fruits.split(',')[1])   
print(fruits.split(',')[2])   
print(fruits.split(',')[3])   
print(fruits.split(',')[4])   
  

print(fruits[0:5]+fruits[25:])
name= input('What is your first name?')
dob= 2022-int(input('What year were you born?'))

print('You are {} years old'.format(dob))