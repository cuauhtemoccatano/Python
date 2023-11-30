# Ejercicio 1

number = float(input("Enter a number: "))

if number > 0:
    print("Positive Number")
else:
    print("Negative Number")

# Ejercicio 2

number = int(input("Enter a number: "))

if number in range(1, 7):
    print("The number is in range")
else:
    print("The number is out of range")

# Ejercicio 3

number = float(input("Ingrese un número: "))
interest = float(input("Ingrese el interés: \n (Valores entre 0 y 100) "))
if interest >= 30:
    print((number * interest/100)+number)
else:
    print(number)
