repeat = True
while repeat:
    print("The Love Calculator is calculating your score...")
    name1 = input("¿What is your name? \n ")
    name2 = input("¿What is their name? \n ")
    combined_names = name1 + name2
    lower_names = combined_names.lower()


    t = lower_names.count("t")
    r = lower_names.count("r")
    u = lower_names.count("u")
    e = lower_names.count("e")
    first_digit = t + r + u + e


    l = lower_names.count("l")
    o = lower_names.count("o")
    v = lower_names.count("v")
    e = lower_names.count("e")
    second_digit = l + o + v + e

    combined_numbers = int(str(first_digit) + str(second_digit))


    if (combined_numbers < 10) or (combined_numbers > 90):
        print(f"Your score is {combined_numbers}, you go together like coke and mentos.")

    elif (combined_numbers >= 40) and (combined_numbers <= 50):
        print(f"Your score is {combined_numbers}, you are alright together.")

    else:
        print(f"Your score is {combined_numbers}.")

    other_names = input("Do you want to calculate other names? Type Y or N .\n").upper()
    if other_names == "Y":
        repeat = True
    else:
        print("See you on the next calculation.")
        repeat = False
