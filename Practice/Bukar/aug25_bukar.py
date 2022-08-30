Cars = [
    {'name':'Mercedes','founder':'Paul Daimler'},
    {'name':'Toyota','founder':'kiichiro toyoda'},
    {'name':'Ferrari','founder':'Enzo Ferrari'}
]

for u in Cars:
    print(f"Founder:{u.get('founder')}")

for u in Cars:
    print(f"Founder:{u.get('founder').split()[-1]}")


