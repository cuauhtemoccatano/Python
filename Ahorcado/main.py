import ahorcado_diagramas as diagramas
import palabras as palabra_adivinar

adivina = palabra_adivinar.seleccion_palabra()
# Invoca la funcion seleccion_palabra y guarda el valor en la variable adivina
nombre = input("Ingresa tu nombre: ")  # Pide el nombre del usuario y lo guarda en la variable nombre
letras_ingresadas = ""  # Variable que guarda las letras ingresadas por el usuario

intentos = 7 # Variable que guarda los intentos del usuario
while intentos > 0:  # Ciclo que se ejecuta mientras los intentos sean mayor a 0
    fallaste = 0  # Variable que guarda los fallos del usuario
    for letra in adivina: # Ciclo que se ejecuta mientras letra este en adivina
        if letra in letras_ingresadas:   # Si letra está en letras_ingresada imprime letra
            print(letra,end="") # Imprime letra y no hace salto de linea con end=""
        else:
            print("_",end="") # Imprime un guion bajo y no hace salto de linea con end=""
            fallaste +=1 # Aumenta en 1 la variable fallaste
    print("") # Imprime un salto de linea
    if fallaste == 0: # Si fallaste es igual a 0
        palabra_adivinar.ganaste(nombre) # Invoca la funcion ganaste
        break # Termina el ciclo while ya que adivino la palabra y no es necesario seguir jugando
    letra_usuario = input("Introduce la palabra o letra que pueda contener la palabra a adivinar: ")
    # Pide una letra o palabra al usuario y la guarda en la variable letra_usuario
    letras_ingresadas += letra_usuario
    # Agrega la letra o palabra ingresada por el usuario a la variable letras_ingresadas

    if letra_usuario not in adivina: # Si la letra o palabra ingresada por el usuario no esta en adivina
        intentos -=1 # Disminuye en 1 la variable intentos
        print("La letra o palabra no esta en la palabra a adivinar")
        # Imprime el mensaje "La letra o palabra no esta en la palabra a adivinar"
    if intentos == 0:
        # Si intentos es igual a 0
        palabra_adivinar.perdiste(nombre,adivina)
        # Invoca la funcion perdiste
    print(f"Te quedan {intentos} intentos")
    # Imprime y concatena el mensaje "Te quedan" con la variable intentos
    diagramas.imprimir(intentos)
    #Invoca funcion imprimir de diagramas_ahorcado.py y pasa como parametro  variable intentos
