for lista in range(1, 101):

    if lista % 3 == 0 and lista % 5 == 0:
        print("FizzBuzz")
    elif lista % 3 == 0:
        print("Fizz")
    elif lista % 5 == 0:
        print("Buzz")
    else:
        print(lista)
