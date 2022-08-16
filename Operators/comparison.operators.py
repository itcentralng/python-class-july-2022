"""
What comparison operators?

    Comparison operators are used to compare two or more elements.
    It returns True if the comparison is valid or False when it is not.
"""

# Operators

"""
>
<
==
>=
<=
"""

# Examples

kubar = {"height":20, "weight":50, "color":"black"}
mustapha = {"height":20, "weight":59, "color":"black"}
bello = {"height":19, "weight":45, "color":"black"}
khalil = {"height":100, "weight":145, "color":"white"}

print(kubar["height"] > mustapha["height"])
print(kubar["color"] == mustapha["color"])
print(khalil["weight"] >= bello["height"])