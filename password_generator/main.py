# Password Generator Project

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v',
           'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R',
           'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

repeat = True
while repeat:

    print("Welcome to the PyPassword Generator!")
    nr_letters = int(input("How many letters would you like in your password?\n"))
    nr_symbols = int(input("How many symbols would you like?\n"))
    nr_numbers = int(input("How many numbers would you like?\n"))

    password_list = []

    for _ in range(nr_letters):
        password_list.append(random.choice(letters))
    for _ in range(nr_symbols):
        password_list.append(random.choice(symbols))
    for _ in range(nr_numbers):
        password_list.append(random.choice(
            numbers))  # Randomly selects a letter, symbol or number from the list and appends it to the password_list

    random.shuffle(password_list)  # changes the order of the list

    password = "".join(password_list)  # uses join to combine all the elements in the list into a string
    print(password)

    another_password = input("Do you want to Generate another password? Type Y for Yes or N for No.").upper()
    if another_password == "Y":
        repeat = True
    else:
        print("See you next time")
        repeat = False
