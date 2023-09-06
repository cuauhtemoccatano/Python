cadena = "Hola Mundo"
print(cadena.count("mundo"))
"""El método count() retorna el número de veces que se
repite un conjunto de caracteres especificado."""

cadena = "Hola Mundo"
print(cadena.find("mundo"))

""" Los metodos find() e index() retornan la ubicación
#(comenzando desde cero) en la que se encuetra el argumento indicado en la cadena."""

cadena = "Hola Mundo"
print(cadena.index("Mundo"))
# este método marca error si no encuentra la subcadena(substring)

cadena = "Hola Mundo"
print(cadena.replace("Mundo", "World"))
# reemplaza temporalmente un campo de la variable

cadena = cadena.replace("Mundo", "World")
# reemplaza el campo de variable

# diferencias entre variable de trabajo, acumulador y  con una explicación detallada de cada una de ellas.
# variable de trabajo: es la variable que se usa para realizar una operación
# acumulador: es la variable que se usa para acumular un valor
# variable de control: es la variable que se usa para controlar un ciclo

cadena = "Hola Mundo"
print("Hola Mundo".split())
print("Hola Mundo".split("."))
print(cadena.split())

"""el metodo de division de una cadena segun un caracter separador
más empleado es split(), cuyo separador es un espacio en blanco y saltos de linea"""

# lista corchetes []
# tupla parentesis ()
# diccionario llaves {}

cadena = "Hola Mundo"
print(cadena.join("Vamos" "a" "ver"))
print(cadena[::-1])
"""el método join() es el inverso de split(), se usa para unir los elementos de una lista y debe ser llamado
desde una cadena que será el separador de los elementos de la lista"""

cadena = "Hola Mundo"
print(len(cadena))
# el método len() retorna la longitud de una cadena, el equivalente de.length en java

cadena = "Hola Mundo"
'''print(cadena[inicio:fin])'''
print(cadena[2:5])
# esta función es exclusiva en el fin(5) y no se incluye en el resultado

cadena = "Hola Mundo"
'''print(cadena[inicio:fin:incremento])'''
print(cadena[2:6:3])
# el incremento es el salto de caracteres que se da en la cadena

cadena = "Hola Mundo"
print(cadena[-3])
# el índice negativo comienza desde el final de la cadena y el primer caracter es -1
