""" Decoradores
def funcion_decoradora(Mi_funcion):
    def invoca_a_Mi_funcion():
        print("Antes de la ejecución de la función a decorar")
        Mi_funcion()
        print("Después de la ejecución de la función a decorar")
    return invoca_a_Mi_funcion

def funcion_decoradora_con_parametros(Mi_funcion):
    def invoca_a_mi_funcion(cadena):
        print("Antes de la ejecución de la función a decorar")
        Mi_funcion(cadena)
        print("Después de la ejecución de la función a decorar")
    return invoca_a_mi_funcion

@funcion_decoradora_con_parametros
def nombre(nombre):
    print("Mi nombre es: ", nombre)



@funcion_decoradora
def saludar():
    print("Hola mundo")


saludar()
nombre(input("Ingrese su nombre: "))

def decorador_sumador(funcion_suma):
    def invoca_a_suma(a,b,c):
        print("se llamará a la funcion suma")
        c = funcion_suma(a,b,c)
        print("se ha llamado a la función suma")
        return c
    return invoca_a_suma
@decorador_sumador
def sumar(a,b,c):
    print("Entra a la función suma")
    return a+b+c
print("Resultado de la suma " ,sumar(1, 2, 3))
"""
#(lambda x: x**2)(2)
#print((lambda x: x**2)(float(input("Ingrese un número: "))))
#print((lambda num1,num2: num1+num2)(float(input("Ingrese un número: ")) ,float(input("Ingrese un número: "))))
# Sintaxis if lambda <arguments> : <Return Value if condition is True> if <condition> else <Return Value if condition is False>
#checar = lambda x: True if (x > 10 and x < 20) else False
#print(checar(15))
#x = int(input("Enter a number: "))
#for i in range(1,11):
 #   print(f"{x} x {i}")
#(lambda x: [print(f"{x} x {i} = {x*i}") for i in range(1,11)])(int(input("Enter a number: ")))

nums = [2,3,5,7]
num_cubes = [num**3 for num in nums] # List comprehension
print(num_cubes) # List comprehension

print([x for x in [1, 2, 3, 4, 5, 6, 7, 8, 9, 10] if x % 2 != 0])
print([num ** 3 for num in nums if num ** 3 > 100])  # List comprehension with if condition

def p(n):
    for number in range(0,n):
        if number % 2 == 0:
            yield number
generator = p(10)
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
print(next(generator))
