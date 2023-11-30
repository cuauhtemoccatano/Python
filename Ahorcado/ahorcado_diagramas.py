#Muestra el dibujo del ahorcado
#Funcion que se invoca cada vez que pierde un intento
def imprimir(intentos): # Recibe como parametro la variable intentos
    if intentos == 0: # Si intentos es igual a 0
        print("""
                       ______
                      |       |
                     _O/      |
                      |       |
                     / \      |
            ______////\\\\____|
        """) # Imprime el dibujo del ahorcado
    elif intentos == 1: # Si intentos es igual a 1
        print("""
                       ___
                      |   |
                     _O/  |
                      |   |
                       \  |
                    ______|
        """) # Imprime el dibujo del ahorcado
    elif intentos == 2: # Si intentos es igual a 2
        print("""
                       ___
                      |   |
                     _O/  |
                      |   |
                          |
                    ______|
        """) # Imprime el dibujo del ahorcado
    elif intentos == 3: # Si intentos es igual a 3
        print("""
                       ___
                      |   |
                     _O/  |
                          |
                          |
                    ______|
        """) # Imprime el dibujo del ahorcado
    elif intentos == 4: # Si intentos es igual a 4
        print("""
                       ___
                      |   |
                      O/  |
                          |
                          |
                    ______|
        """)  # Imprime el dibujo del ahorcado
    elif intentos == 5: # Si intentos es igual a 5
        print("""
                       ___
                      |   |
                      O   |
                          |
                          |
                    ______|
        """) # Imprime el dibujo del ahorcado
    elif intentos == 6: # Si intentos es igual a 6
        print("""
                       ___
                      |   |
                          |
                          |
                          |
                    ______|
        """) # Imprime el dibujo del ahorcado
    elif intentos == 7: # Si intentos es igual a 7
        print("""
                    
                      
                          
                          
                          
                    ______
        """)
