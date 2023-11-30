# Description: Este archivo contiene las funciones que se encargan de seleccionar la palabra a adivinar
# y de mostrar el mensaje de victoria o derrota
import random # Importa la libreria random

def seleccion_palabra(): # Funcion que se encarga de seleccionar la palabra a adivinar
    print("Juego del Ahorcado") # Imprime el mensaje "Juego del Ahorcado" y presenta las instrucciones en los siguientes print
    print("Instrucciones: El juego consiste en adivinar una palabra, tienes 7 intentos para adivinar la palabra")
    print("Si adivinas la palabra ganas, si no pierdes")
    print("Puedes ingresar una letra o una palabra, Si ingresas una palabra y esta es igual a la palabra a adivinar ganas")
    print("Si la letra ingresada no está en la palabra, pierdes un intento")
    print("Si repites una letra o palabra, pierdes un intento")
    print("Si ingresas mas de una letra o palabra pierdes un intento")

    lista = ["hola", "mundo", "python", "programacion", "computadora", "teclado", "mouse", "monitor", "ventana", "casa",
             "perro", "gato", "pajaro", "pelicula", "musica", "videojuego", "celular", "telefono", "internet", "redes",
             "programa", "libro", "cuaderno", "lapiz", "pluma", "escritorio", "silla", "mesa", "cama", "almohada"]
    # Lista de palabras a adivinar

    palabra = random.choice(lista) # Selecciona una palabra aleatoria de la lista y la guarda en la variable palabra
    return palabra # Regresa la variable palabra


def ganaste(nombre): # Funcion que se invoca cuando gana el usuario
    print(f"Muchas Felicidades por tu victoria, {nombre}")
    # Imprime el mensaje "Muchas Felicidades por tu victoria" y concatena el nombre del usuario
    return "" # Regresa un string vacio


def perdiste(nombre,palabra): # Funcion que se invoca cuando pierde el usuario
    print(f"Acabas de perder {nombre}, la palabra correcta era \'{palabra}\', sigue participando ")
    # Imprime el mensaje "Acabas de perder" y concatena el nombre del usuario y la palabra que no pudo adivinar
    return "" # Regresa un string vacio
