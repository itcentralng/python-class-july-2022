fruits=[{'name':'Apple', 'taste':6.5, 'colour':'red'}, #taste score /10
        {'name':'Pear', 'taste':8, 'colour':'green'},
        {'name':'Grapes', 'taste':7.5, 'colour':'purple'},
        {'name':'Orange', 'taste':7.5, 'colour':'orange'},
        {'name':'Tomato', 'taste':5, 'colour':'red'},]

#print(fruits)

fruits[0]['price']= 'N10'
fruits[1]['price']= 'N15'
fruits[2]['price']= 'N20'
fruits[3]['price']= 'N25'
fruits[4]['price']= 'N30'

print('{}: this is a {} and {} in colour'.format(fruits[0]['name'], fruits[0]['taste'], fruits[0]['colour'], fruits[0]['price']))
print('{}: this is an {} and {} in colour'.format(fruits[1]['name'], fruits[1]['taste'], fruits[1]['colour'], fruits[1]['price']))
print('{}: this is a {} and {} in colour'.format(fruits[2]['name'], fruits[2]['taste'], fruits[2]['colour'], fruits[2]['price']))
print('{}: this is a {} and {} in colour'.format(fruits[3]['name'], fruits[3]['taste'], fruits[3]['colour'], fruits[3]['price']))
print('{}: this is a {} and {} in colour'.format(fruits[4]['name'], fruits[4]['taste'], fruits[4]['colour'], fruits[4]['price']))

