
""" Ejercicio 1
Escribir un programa que convierta un valor dado en grados Fahrenheit a grados Celsius.
Recordar que la fórmula para la conversión es:([°F] − 32) × 5 ⁄ 9 """

fahrenheit = float(input ("Dame grados Fahrenheit "))
print("Los grados celsius son:",(fahrenheit - 32) *5 /9)

"""Ejercicio 2 
Dados dos números, mostrar la suma, resta, división y multiplicación de ambos. """

numero1 = float(input("Dame el primer numero"))
numero2 = float(input("Dame el segundo numero"))
print("La suma es: ",numero1+numero2)
print("La resta es:", numero1-numero2)
print("La multiplicación es: ",numero1*numero2)
print("La división es:", numero1/numero2)

"""Ejercicio 3 
Calcular el perímetro y área de un rectángulo dada su base y su altura."""

numero1 = float(input("Dame el largo del rectángulo "))
numero2 = float(input("Dame el alto del número "))
print("El perimetro es: ", (numero1*2)+(numero2*2))
print("El area es: ", numero1*numero2/2)

"""Ejercicio 4
Calcular la media de tres números pedidos por teclado."""

numero1 = float(input("Dame el primer numero"))
numero2 = float(input("Dame el segundo numero"))
numero3 = float(input("Dame el tercer numero"))
print("La media de los 3 numeros es: ", numero1+numero2+numero3/3)
