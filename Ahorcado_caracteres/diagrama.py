#Muestra el dibujo del ahorcado
#Funcion que se invoca cada vez que pierde un intento
def imprimir(intentos):
    if intentos == 1:
        print("""
                       ___
                      |   |
                     _O/  |
                      |   |
                     / \  |
                    ______|
        """)
    elif intentos == 2:
        print("""
                       ___
                      |   |
                     _O/  |
                      |   |
                       \  |
                    ______|
        """)
    elif intentos == 3:
        print("""
                       ___
                      |   |
                     _O/  |
                      |   |
                          |
                    ______|
        """)
    elif intentos == 4:
        print("""
                       ___
                      |   |
                     _O/  |
                          |
                          |
                    ______|
        """)
    elif intentos == 5:
        print("""
                       ___
                      |   |
                      O/  |
                          |
                          |
                    ______|
        """)
    elif intentos == 6:
        print("""
                       ___
                      |   |
                      O   |
                          |
                          |
                    ______|
        """)
