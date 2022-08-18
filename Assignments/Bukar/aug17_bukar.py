animals = {
  'lion':'a large tawny coloured cat',
  'cat':'a small domesticated,carnivorous animal',
  'bird':'An animal that flies'}
for b in range(10):
    word = input('Search the meaning of an Animal: ')
    word = word.lower().strip()
    if animals.get(word):
        print(animals.get(word))
    else:
        print('Animal not found')



