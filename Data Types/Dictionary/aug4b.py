# Exercise

"""
1. Create a dictionary holding your personal information like; 
    name, address, phone number, age, date of birth, place of birth, work experience, schools attended
2. Print out your personal information in this format:
    1. Name: John Doe
    2. Address: 123 Main Street
    3. Phone Number: 080-123-4567
    4. Age: 20
    5. Date of Birth: 12/12/2000
    6. Place of Birth: Lagos
    7. Work Experience: 1 year
    8. Schools Attended: School of Science, School of Engineering, School of Business
"""

# SOLUTIION

personalinfo = {
    "name":"Kyle Johnson",
    "address": "39 Kuwait Crescent, Kaduna",
    "phone":"+2349012345678",
    "state":"Lagos",
    "age":15,
    "dob":"20-07-2007",
    "pob":"Katsina",
    "work":"5 Years",
    "schools":["Darulhuda", "Command Secondary School", "Bayero University"]
}
print("\n")
print(
    """
    1. Name: {}
    2. Address: {}
    3. Place of Birth: {}
    4. Work Experience: {}
    5. Schools Attended: My primary school is {}, my secondary school is {} and my university if {}
    """.format(personalinfo["name"], personalinfo["address"], personalinfo["pob"], personalinfo["work"], personalinfo["schools"][0], personalinfo["schools"][1], personalinfo["schools"][2])
)