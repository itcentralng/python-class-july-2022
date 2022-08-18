animals = {'lion':'a large tawny coloured cat', 'cat':'a small domesticated,carnivorous animal', 'bird':'An animal that flies'}

word = input('Search the meaning of an Animal: ')

for u in animals:
    if word in animals:
        print(animals['lion'],animals['cat'],animals['bird'])
    else:
        print('Animal not found')