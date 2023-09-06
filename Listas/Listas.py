mi_lista = ['H', 1, 3.3, "hola", False]
print(mi_lista[2])
print(mi_lista[4]*2)
print(mi_lista)
# se pueden multiplicar números por datos booleanos y se convierten en 1 o 0

mi_lista = ['H', 1, 3.3, "hola", False]
mi_lista.append("otro")
# agrega un elemento al final de la lista
print(mi_lista)
mi_lista.insert(2, "nuevo") # agrega un elemento en la posición 2
# agrega un elemento en la posición 2
print(mi_lista)
mi_lista.insert(-1, "ultimo")
# agrega un elemento en la posición -1
print(mi_lista)
'''mi_lista[10]= "PILARES"
mi_lista[10]= "PILARES"
IndexError: list assignment index out of range'''
mi_lista[3]= "PILARES"
print(mi_lista)
mi_lista.remove("PILARES")
# elimina el elemento "PILARES"
print(mi_lista)
mi_lista.pop(2)
# elimina el elemento en la posición 2
mi_lista.pop()
# elimina el último elemento
print("Longitud de la lista: ", len(mi_lista))