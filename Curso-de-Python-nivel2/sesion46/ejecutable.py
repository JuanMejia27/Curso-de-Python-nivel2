def sumar(a, b):
    """Suma de dos valores"""
    return a + b


x = 10
print(sumar(x, 5))

x = {"key": "value", "another_key": "another_value"}


def saludo(nombre):
    """Impresion de valores"""
    print(f"Hola {nombre}")


if __name__ == "__main__":
    '''Ejecuta el codigo si es llamado desde la terminal'''
    saludo("Mundo")
    x = [1, 2, 3]
    for i in x:
        print(i)
