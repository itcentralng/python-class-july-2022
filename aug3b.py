# SOLUTION

# 1. Create a list of 3 students

students = [
    [
        "Khalil", 20, 
        ["eating", "drinking", "cooking"]
    ], 
    [
        "Bukar", 19, 
        ["swimming", "jumping", "reading"]
    ], 
    [
        "Mustapha", 18, 
        ["traveling", "hiking", "flying"]
    ]
]

print("My name is {}, I am {} years old and I enjoy {}, {} and {}".format(students[0][0], students[0][1], students[0][2][0], students[0][2][1], students[0][2][2]))
print("My name is {}, I am {} years old and I enjoy {}, {} and {}".format(students[1][0], students[1][1], students[1][2][0], students[1][2][1], students[1][2][2]))
print("My name is {}, I am {} years old and I enjoy {}, {} and {}".format(students[2][0], students[2][1], students[2][2][0], students[2][2][1], students[2][2][2]))