"""
Yasir is a teacher at IT Central and he wants you to write a loop
that will help him call all his books one by one and print them
including their authors. In this format:

Book: Harry Potter and the Deathly Hallows Author: JK Rowlings
"""

books = [
    {"name":"12 Rules for life","author":{"title":"Dr.", "name":"Jordan Peterson"}},
    {"name":"How to win friends and influence people","author":{"title":"Mr.", "name":"Dale Carnegie"}},
    {"name":"Discover your destiny","author":{"title":"Mr.", "name":"Robin Sharman"}},
    {"name":"Atomic Habits","author":{"title":"Mr.", "name":"James Clear"}},
    {"name":"Gifted Hands","author":{"title":"Dr.", "name":"Ben Carson"}},
    ]

# for book in books:
#     print("Book: {} Author: {}".format(book.get('name'), book.get('author')))

"""
Yasir has changed his mind, he wants you to print the authors' 
last names only. In this format:
Author: Mr. Clear
"""

for book in books:
    print(f"Author: {book.get('author')}")