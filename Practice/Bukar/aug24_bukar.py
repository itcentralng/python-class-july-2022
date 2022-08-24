from webbrowser import get


books = [
    {'name':'out of his mind','author':'alamu moses'},
    {'name':'python programming','author':'adam steward'},
    {'name':'the costly mistake','author':'nicole chinlo'}
]

for u in books:
    print(f"author:{u.get('author').split()[-1]}")