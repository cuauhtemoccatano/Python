mi_diccionario = {"nombre": "Juan", "apellido": "Perez", "edad": 25}
'''la sintaxis es clave:valor y se separan por comas 
# y se encierran en llaves {}'''
print(mi_diccionario["nombre"])  # se accede a los valores por la clave y se encierran en corchetes
print(len(mi_diccionario))
mi_diccionario.pop("nombre")
print(mi_diccionario)
print(mi_diccionario.keys())  # devuelve una lista de las claves
print(mi_diccionario.values())  # devuelve una lista de los valores
print(mi_diccionario.items())  # devuelve una lista de tuplas
print(f" Estos Elementos {mi_diccionario} pertenecen a mi diccionario")  # f sirve para concatenar
print("Elementos de mi diccionario son", mi_diccionario)  # se puede concatenar con coma
print(mi_diccionario.get("nombre"))  # devuelve el valor de la clave
print(mi_diccionario["edad"])