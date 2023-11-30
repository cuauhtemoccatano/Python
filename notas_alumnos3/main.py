'''Codifica un programa en Python que nos permita guardar los nombres de los alumnos de una clase y las notas que han obtenido.
Cada alumno puede tener distinta cantidad de notas.
Guarda la información en un diccionario cuya claves serán los nombres de los alumnos y los valores serán listados con las notas de cada alumno.

El programa pedirá el número de alumnos que vamos a introducir, pedirá su nombre e irá pidiendo sus notas hasta que introduzcamos un número negativo.
Al final el programa nos mostrará la lista de alumnos y la nota media obtenida por cada uno de ellos.
Nota: si se introduce el nombre de un alumno que ya existe el programa nos dará un error.'''


from statistics import mean

def main():
    alumnos = {}
    num_alumnos = int(input("Introduce el número de alumnos: "))
    for i in range(num_alumnos):
        nombre = input("Introduce el nombre del alumno: ")
        notas = []
        nota = float(input("Introduce la nota del alumno: "))
        while nota >= 0:
            notas.append(nota)
            nota = float(input("Introduce la nota del alumno: "))
        alumnos[nombre] = notas
    for nombre, notas in alumnos.items():
        print("%s ha sacado de media %.2f" % (nombre, mean(notas)))
