measure = True
while measure:

    height = float(input("Enter your height in meters \n e.g., 1.55 \n"))
    weight = float(input("Enter your weight in kg \n e.g., 60.54 \n"))

    bmi = weight / (height * height)
    if bmi < 18.5:
        print(f"Your BMI is {bmi},you are underweight.")

    elif bmi < 25:
        print(f"Your BMI is {bmi}, you have a normal weight.")

    elif bmi < 30:
        print(f"Your BMI is {bmi}, you are slightly overweight.")

    elif bmi < 35:
        print(f"Your BMI is {bmi}, you are obese.")
    else:
        print(f"Your BMI is {bmi}, you are clinically obese.")

    measure_again = input("Do you want to measure another BMI? Type 'y' or 'n' ").upper()
    if measure_again == "Y":
        measure = True
    else:
        print("Thank you for using our BMI calculator.")
        measure = False
