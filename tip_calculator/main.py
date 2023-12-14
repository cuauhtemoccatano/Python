
repeat = True
while repeat:
    print("Welcome to the tip calculator.")

    total_bill = float(input("¿What was the total bill? \n $"))

    tip = float(input("¿What percentage tip would you like to give?(Enter a number between 0-100) \n %"))

    tip_total = (total_bill * tip) / 100

    people = int(input("How many people to split the bill? \n "))
    person_total = (total_bill + tip_total) / people

    print(f"Each person should pay: $ {round(person_total,2)}.")
    another_bill = input("Do you want to calculate another bill? (Y/N) \n").upper()
    if another_bill == "Y":
        repeat = True
    else:
        print("See you next time!")
        repeat = False
