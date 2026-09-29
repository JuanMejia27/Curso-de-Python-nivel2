def decorador(func):
    def decorador_decorado():
        print("Algo se esta haciendo antes de ejecutar la funcion")
        func()
        print("Algo se esta haciendo despues de ejecutar la funcion")
    return decorador_decorado

@decorador #Este ayuda a mejorar la funcion
def mi_funcion():
    print("Ejecutando la funcion principal")
mi_funcion()

'''mi_funcion = decorador(mi_funcion)
mi_funcion()'''

def decorador_con_parametros(func):
    def funcion_decorada(a,b):
        print(f"Antes de ejecutar con parametros {a} y {b}")
        resultado = func(a,b)
        print(f"Despues de ejecutar con parametros {a} y {b}")
        return resultado
    return funcion_decorada

@decorador_con_parametros
def suma(a,b):
    return a + b

suma(5,7)

def decorador_1(func):
    def inner_1():
        print("Ejecutando decorador 1")
        return func()
    return inner_1

def decorador_2(func):
    def inner_2():
        print("Ejecutando decorador 2")
        return func()
    return inner_2

@decorador_1
@decorador_2
def mi_funcion():
    print("Ejecutando funcion original")

mi_funcion()

def decorador_multiplicador(func):
    def inner(num):
        resultado = func(num)
        return resultado * 2
    return inner

@decorador_multiplicador
def obtener_numero(numero):
    return numero

print(obtener_numero(7))


def log(func):
    def inner(*args, **kwargs):
        print(f"Llamada a la funcion {func.__name__} con los argumentos {args} y {kwargs}")
        return func(*args, **kwargs)
    return inner

@log
def saludar(nombre):
    print(f"Hola, {nombre}")

saludar("Juan")