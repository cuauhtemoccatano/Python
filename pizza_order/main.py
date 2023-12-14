order = True
while order:
    print("Thank you for choosing Python Pizza Deliveries!")
    size = input("¿What size of pizza do you want? \n S, M, L \n ").upper()
    add_pepperoni = input("¿Do you want pepperoni? \n Y or N \n ").upper()
    extra_cheese = input("¿Do you want extra cheese? \n Y or N \n ").upper()

    bill = 0
    if size == "S":
        bill = 15
    elif size == "M":
        bill = 20
    else:
        bill = 25
    if add_pepperoni == "Y":
        if size == "S":
            bill += 2
        else:
            bill += 3

    if extra_cheese == "Y":
        bill += 1

    print(f"Your final bill is: ${bill}.")

    another_order = input("¿Do you want to make another order? \n Y or N").upper()
    if another_order == "Y":
        order = True
    else:
        print("Enjoy your order!\n See you soon!")
        order = False
