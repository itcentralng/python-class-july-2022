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
# .clear
fruit.clear()
print(fruit)
# .setdefault
print(fruit.setdefault("weight", "5 grams"))
fruit["height"] = "5CM"
print(fruit)
# .update
fruit.update(color="red")
print(fruit)
# .copy
fruit1 = fruit.copy()
print(fruit1)
# .fromkeys
fruit2 = fruit.fromkeys(("name", ), "Pawpaw")
print(fruit2)
# .popitem
print(fruit2.popitem())
print(fruit2)