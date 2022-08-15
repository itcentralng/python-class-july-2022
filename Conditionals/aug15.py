"""
What are conditional statements?

    Conditional statements are used to perform different actions based on different conditions.
    For example to check if a student is eligible for admission or not.
"""

# Conditional Statements
"""
1) IF
    If the condition is True, then the statement is executed.
2) ELSE
    If the condition is False, then the statement is executed.
3) ELSE IF
    If the condition is False, then the statement is executed.
    If the condition is True, then the statement is not executed.
4) NESTED IF
    If the condition is True, then the statement is executed.
    If the condition is False, then the statement is not executed.
"""


# Example

# # IF and ELSE
students = ["001", "002", "003", "004"]

if "001" in students:
    print("001 is present in the list")
else:
    print("001 is not present in the list")

# # ELSE IF

if "001" in students:
    print("001 is present in the list")
elif "005" in students:
    print("005 is present in the list")
elif "004" in students:
    print("004 is present in the list")
else:
    print("No student is present in the list")


# MORE EXAMPLES

if "001" in students:
    print("001 is present in the list")
if "002" in students:
    print("002 is present in the list")
if "003" in students:
    print("003 is present in the list")