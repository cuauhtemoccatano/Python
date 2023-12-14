repeat = True
while repeat:

    print("Welcome to FizzBuzz")
    target = int(input("Enter the number you want to check: \n "))
    for numbers in range(target + 1):

        if numbers % 3 == 0 and numbers % 5 == 0:
            print("FizzBuzz")
        elif numbers % 3 == 0:
            print("Fizz")
        elif numbers % 5 == 0:
            print("Buzz")
        else:
            print(numbers)

    other_number = input("Do you want to check another number? \n (Y/N)").upper()
    if other_number == "Y":
        repeat = True
    else:
        print("See you next time!")
        repeat = False
