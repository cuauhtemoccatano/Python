#Necesito hacer un ahorcado, las palabras van a ser asignadas por el  usuario, y solo tendra 6 intentos para completar el juego
#Tambien necesito que el usuario pueda ingresar una letra y que el programa le diga si esta o no en la palabra
#Si la letra esta en la palabra, se debe mostrar en que posicion esta la letra
#Si la letra no esta en la palabra, se debe mostrar un mensaje de error y se debe restar un intento
# y debe dibujar una parte del ahorcado
#Si el usuario adivina la palabra, debe mostrar un mensaje de felicitaciones
#Si el usuario no adivina la palabra, debe mostrar un mensaje de que perdio el juego
# y mostrar la palabra correcta
#Si el usuario se queda sin intentos, debe mostrar un mensaje de que perdio el juego
# y mostrar la palabra correcta

import random
import os
import time
import diagrama as dibujo

def clear():
    os.system('cls')

def imprimir(intentos):
    if intentos == 1:
        dibujo.imprimir1()
    elif intentos == 2:
        dibujo.imprimir2()
    elif intentos == 3:
        dibujo.imprimir3()
    elif intentos == 4:
        dibujo.imprimir4()
    elif intentos == 5:
        dibujo.imprimir5()
    elif intentos == 6:
        dibujo.imprimir6()

def ahorcado():
    #Lista de palabras
    palabras = ["hola", "mundo", "python", "programacion", "computadora", "teclado", "mouse", "monitor", "ventana", "casa", "perro", "gato", "pajaro", "pelicula", "musica", "videojuego", "celular", "telefono", "internet", "redes", "programa", "libro", "cuaderno", "lapiz", "pluma", "escritorio", "silla", "mesa", "cama", "almohada"]
    #Palabra a adivinar
    palabra = random.choice(palabras)
    #Palabra a mostrar
    palabra_mostrar = []
    #Palabra a mostrar en string
    palabra_mostrar_str = ""
    #Intentos
    intentos = 0
    #Letras adivinadas
    letras_adivinadas = []
    #Letra ingresada
    letra = ""
    #Variable para saber si gano o no
    gano = False
    #Variable para saber si quiere volver a jugar
    jugar = True
