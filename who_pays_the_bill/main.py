import random
repeat = True
while repeat:
    names_string = input("Give me everybody's names, separated by a comma: \n ").upper()
    names = names_string.split(", ")
    rand_idx = random.randrange(len(names))
    who_pays = names[rand_idx]
    print(f"{who_pays} is going to buy the meal today!")

    other_name = input("Do you want another name? Type Y or N: ").upper()
    if other_name == "Y":
        repeat = True
    else:
        print("See you on the next meal!")
        repeat = False
