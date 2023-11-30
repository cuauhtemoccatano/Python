"""Programa que calcule el interés de una cantidad si es mayor al 30%, si no informa el importe total."""
number = float(input("Ingrese un número: "))
interest = float(input("Ingrese el interés: \n (Valores entre 0 y 100) "))
if interest >= 30:
    print((number * interest/100)+number)
else:
    print(number)
