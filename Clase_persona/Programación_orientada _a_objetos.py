"""Vamos a crear una clase llamada Persona. Sus atributos son: nombre, edad y DNI. Construye los siguientes métodos para la clase:

Un constructor, donde los datos pueden estar vacíos.

Los setters y getters para cada uno de los atributos. Hay que validar las entradas de datos.

mostrar(): Muestra los datos de la persona.

esMayorDeEdad(): Devuelve un valor lógico indicando si es mayor de edad"""


class Persona:

        def __init__(self, nombre = "", edad = 0, dni = ""):
            self.nombre = nombre
            self.edad = edad
            self.dni = dni

        def __str__(self):
            return f"Nombre: {self.nombre}, Edad: {self.edad}, DNI: {self.dni}"


        def set_nombre(self, nombre):
            self.nombre = nombre

        def get_nombre(self):
            return self.nombre

        def set_edad(self, edad):
            self.edad = edad

        def get_edad(self):
            return self.edad

        def set_dni(self, dni):
            self.dni = dni

        def get_dni(self):
            return self.dni

        def mostrar(self):
            return f"Nombre: {self.nombre}, Edad: {self.edad}, DNI: {self.dni}"

        if get_edad() >= 25:
            print("Es mayor de edad")
        else:
            print("Es menor de edad")

class Cuenta:

    def __init__(self, titular, cantidad = 0):
        self.titular = titular
        self.cantidad = cantidad

    def __str__(self):
        return f"Titular: {self.titular}, Cantidad: {self.cantidad}"

    def ingresar(self, cantidad):
        if cantidad > 0:
            self.cantidad += cantidad

    def retirar(self, cantidad):
        if cantidad > 0:
            self.cantidad -= cantidad

class CuentaJoven(Cuenta):

    def __init__(self, titular, cantidad = 0, bonificacion = 0):
        super().__init__(titular, cantidad)
        self.bonificacion = bonificacion

    def __str__(self):
        return f"{super().__str__()}, Bonificacion: {self.bonificacion}"

    def es_titular_valido(self):
        return self.titular.es_mayor_edad() and self.titular.edad < 25

    def retirar(self, cantidad):
        if self.es_titular_valido():
            super().retirar(cantidad)

    def mostrar(self):
        return f"Cuenta Joven, {super().__str__()}, Bonificacion: {self.bonificacion}"

#Datos a mostrar:
persona = Persona("Juan", 24)
cuenta = CuentaJoven(persona, 100, 10)
print(cuenta.mostrar())
cuenta.retirar(50)
