"""Crea una tupla con los meses del año, pide números al usuario, si el número está entre 1 y la longitud máxima de la tupla,
muestra el contenido de esa posición sino muestra un mensaje de error.
El programa termina cuando el usuario introduce un cero."""

months = ("January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November","December")
number = int(input("Enter a number between 1 and 12: "))
while number != 0:
    if number > 0 and number <= len(months):
        print(months[number-1])
    else:
        print("Error, the number must be between 1 and 12")
    number = int(input("Enter a number between 1 and 12: "))
