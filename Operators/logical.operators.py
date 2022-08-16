"""
What are logical operators?

    Logical operators are used to combine conditional statements.
    A logical operation is a Boolean expression that evaluates to True or False.
"""

# Logical Operators
"""
1) AND
    Returns True if both operands are True.
    Returns False if either operands is False.
2) OR
    Returns True if either operands is True.
    Returns False if both operands are False.
3) NOT
    Returns True if operand is False.
    Returns False if operand is True.
"""

# Example
a = True
b = False

print(a and b)
print(a or b)
print(not a)

print('\n\n') 

print(a and b and not a)
print(a or b or not a)
print(not a or b or a)