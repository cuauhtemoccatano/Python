class padre():
    def __init__(self, nombre="Saul", edad=35):  # Constructor
        self.nombre_padre = nombre  # Atributo publico
        self.__edad_padre = edad  # Atributo privado

    @property  # Decorador
    def edad(self):  # Metodo get
        return self.__edad_padre  # Retorna el valor del atributo privado

    @edad.setter  # Decorador
    def edad(self, valor):  # Metodo set
        self.__edad_padre = valor  # Asigna el valor al atributo privado


Juan = padre()  # Instancia de la clase padre

print(Juan.nombre_padre)  # Imprime el atributo publico
print(Juan.edad)  # Imprime el atributo privado
