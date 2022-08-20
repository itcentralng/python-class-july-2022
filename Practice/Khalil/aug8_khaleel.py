fruit = {"name":"Apple", "price":100, "taste":"sweet"}
# .items  
"""
"""
print(fruit.items())
# . get  
print(fruit.get("ice"))
# .pop
name = fruit.pop("name")
print(name)
price = fruit.pop("price")
print(price)
# . keys
print(fruit.keys())
# .clear     removes everything from the list
# fruit.clear()
# print(fruit)
# # .setdefault    returns the value of the specified key and 'insert the key, with the specified value' if the key doesnt exist
# print(fruit.setdefault("weight", "5 grams"))
# fruit["height"] = "5CM"
# print(fruit)
# # .update     adds the key value pair to the dictionary
# fruit.update(color="red")
# print(fruit)
# # .copy     returns a copy of the dictionary
# fruit1 = fruit.copy()
# print(fruit1)
# # .fromkeys     returns a dictionary with the chosen keys and values
# fruit2 = fruit.fromkeys(("name", ), "Pawpaw")
# print(fruit2)
# # .popitem      removes the last key-value pair
# print(fruit2.popitem())
# print(fruit2)