"""
What are membership operators?

    Membership operators are used to test if an element is present in an iterable.
    For example to check the exists of a student in a class.
    This returns a Boolean value that is True if the element is present in the set.
"""

# Membership Operators
"""
1) IN
    Returns True if the element is present in the set.
    Returns False if the element is not present in the set.
2) NOT IN
    Returns True if the element is not present in the set.
    Returns False if the element is present in the set.
"""

# Example
student_ids = ["001", "002", "003", "004"]

print("001" in student_ids)
print("005" in student_ids)
print("001" not in student_ids)
print("005" not in student_ids)