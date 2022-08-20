#Dictionary

student= {'name':'Khaleel Bukar Mustapha', 'age':45}
print(student['name'])
print(student['age'])

student['heigt']= '1.8m' #adds the new info to the dictionary
student['weight']= '70kg'
student['friends']= [{'name':'Qasim','age':15},{'name':'Yusuf','age':20}] #dictionaries within a list

print(student['friends'][0]['name'])



