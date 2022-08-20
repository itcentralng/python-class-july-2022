# QUESTIONS 
"""
1. Print out 4 differences between a list and a dictionary
2. Create a list of fruits:
    a. Using your understanding of dictionary create five fruits in the
        list all with a name, taste and color.
    b. Add a new key to each fruit that holds the price of that fruit
3. Print each fruit in this format:
        1. Mango: This is sweet and brown in color
        2. Cashew: This is sour and green in color 
"""

# ANSWERS

# 1.

difference = """
1. A list is a collection of items in a particular order.
2. A dictionary is a collection of key-value pairs.
3. Objects in a list can be accessed using thier index
4. Values in a dictionary can be accessed using thier keys
"""
print(difference)

# 2a. 

fruits = [
    {"name": "Mango", "taste": "sweet", "color": "brown"},
    {"name": "Cashew", "taste": "sour", "color": "green"},
    {"name": "Pineapple", "taste": "sweet", "color": "yellow"},
    {"name": "Apple", "taste": "sweet", "color": "red"},
    {"name": "Banana", "taste": "sweet", "color": "yellow"}
]

# 2b.
fruits[0]["price"] = "₦1.00"
fruits[1]["price"] = "₦0.50"
fruits[2]["price"] = "₦0.75"
fruits[3]["price"] = "₦0.25"
fruits[4]["price"] = "₦0.10"

# 3.

print("{}: This is {} and {} in color. It cost {} only.".format(fruits[0]["name"], fruits[0]["taste"], fruits[0]["color"], fruits[0]["price"]))
print("{}: This is {} and {} in color. It cost {} only.".format(fruits[1]["name"], fruits[1]["taste"], fruits[1]["color"], fruits[1]["price"]))
print("{}: This is {} and {} in color. It cost {} only.".format(fruits[2]["name"], fruits[2]["taste"], fruits[2]["color"], fruits[2]["price"]))
print("{}: This is {} and {} in color. It cost {} only.".format(fruits[3]["name"], fruits[3]["taste"], fruits[3]["color"], fruits[3]["price"]))
print("{}: This is {} and {} in color. It cost {} only.".format(fruits[4]["name"], fruits[4]["taste"], fruits[4]["color"], fruits[4]["price"]))