# IF

cutoffmark = 50

bukar = {"score":45, "name":"Usman Bukar"}
bello = {"score":25, "name":"Yasir Bello"}
khalil = {"score":95, "name":"Khalil Dasuki"}
mustapha = {"score":75, "name":"Mustapha Mustapha"}

if bukar['score'] >= cutoffmark:
    print(bukar["name"], " is admitted")
if bello['score'] >= cutoffmark:
    print(bello["name"], " is admitted")
if khalil['score'] >= cutoffmark:
    print(khalil["name"], " is admitted")
if mustapha['score'] >= cutoffmark:
    print(mustapha["name"], " is admitted")

print("**\n\n**")

# ELSE IF
if bukar['score'] >= cutoffmark:
    print(bukar["name"], " is admitted")
elif bello['score'] >= cutoffmark:
    print(bello["name"], " is admitted")
elif khalil['score'] >= cutoffmark:
    print(khalil["name"], " is admitted")
elif mustapha['score'] >= cutoffmark:
    print(mustapha["name"], " is admitted")

print("**\n\n**")

# ELSE

if bukar['score'] >= cutoffmark:
    print(bukar["name"], " is admitted")
else:
    print(bukar["name"], " is not admitted")
if bello['score'] >= cutoffmark:
    print(bello["name"], " is admitted")
else:
    print(bello["name"], " is not admitted")
if khalil['score'] >= cutoffmark:
    print(khalil["name"], " is admitted")
else:
    print(khalil["name"], " is not admitted")
if mustapha['score'] >= cutoffmark:
    print(mustapha["name"], " is admitted")
else:
    print(mustapha["name"], " is not admitted")