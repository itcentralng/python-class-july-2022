# SET

"""
What is a set in python?

A set is a collection of unique elements.
"""

student_ids = {"001", "002", "003", "001", "002", "004"}
student_ids.add("005")
student_regs = {"006", "002", "007", "004", "005"}
print(student_ids.difference(student_regs))
student_ids.clear()
print(student_ids)