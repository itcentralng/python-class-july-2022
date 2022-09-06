counter = 1 
while(counter <=3):
    principal = int(input("Enter the principal amount: "))
    numberofyears = int(input('Enter the number of years: '))
    rateofinterest = float(input('Enater the rate of interest'))
    simpleinterest = principal*numberofyears*rateofinterest/100
    print("Simple interest = %.2f"% simpleinterest)
    # increse counter by 1
    counter = counter+1
    print("You have calculated simple interest for 3 time!")
    break