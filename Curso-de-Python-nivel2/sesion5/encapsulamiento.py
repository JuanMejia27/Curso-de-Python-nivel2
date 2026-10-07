class CuentaBancaria:
    def __init__(self, saldo = 0):
        self.__saldo = saldo  # Atributo privado
    def deposito(self, cantidad):
        if cantidad > 0:
            self.__saldo += cantidad
            print(f"Depósito exitoso: {cantidad}. Saldo actual: {self.__saldo}")
        else:
            print("Cantidad para depósito inválida.")
    def get_saldo(self):
        return self.__saldo  # Método getter para acceder al saldo privado

cuenta = CuentaBancaria(1000)
print(f"Saldo actual: {cuenta.get_saldo()}")
cuenta.deposito(500)
print(f"Saldo actual: {cuenta.get_saldo()}")

class Circulo:
    def __init__(self, radio):
        self.__radio = radio
    @property
    def radio(self):
        return self.__radio
    @radio.setter
    def radio(self, valor):
        if valor < 0:
            print("El radio no puede ser negativo. Se establecerá a 0.")
            self.__radio = 0
        else:
            self.__radio = valor
    @property
    def area(self):
        return 3.14159 * (self.__radio ** 2)

circulo = Circulo(5)
print(f"Radio: {circulo.radio}, Área: {circulo.area}")
circulo.radio = -3  # Intento de establecer un radio negativo
circulo.radio = 7  # Establecer un radio positivo
print(f"Radio nuevo cambiado: {circulo.radio}")
print(f"Radio: {circulo.radio}, Área: {circulo.area}")

class Persona:
    def __init__(self, nombre, edad):
        self.__nombre = nombre
        self.__edad = edad
    def __repr__(self):
        return f"Persona(nombre {self.__nombre}, edad {self.__edad})"
    '''@property
    def nombre(self):
        return self.__nombre
    @property
    def edad(self):
        return self.__edad
    @edad.setter
    def edad(self, valor):
        if valor < 0:
            print("La edad no puede ser negativa. Se establecerá a 0.")
            self.__edad = 0
        else:
            self.__edad = valor'''
persona = Persona("Esli", 30)
print(repr(persona))

class Milista:
    def __init__(self, elementos):
        self.__elementos = elementos
    def __len__(self): # Sobreescribimos el método __len__ para devolver la longitud de la lista
        return len(self.__elementos)

liusta = Milista([1, 2, 3, 4, 5])
print(f"Longitud de la lista: {len(liusta)}")

class Libro:
    def __init__(self, titulo, autor, año_publicacion, num_paginas):
        self.__titulo = titulo
        self.__autor = autor
        self.__año_publicacion = año_publicacion
        self.__num_paginas = num_paginas
    def __str__(self): # Sobreescribimos el método __str__ para devolver una representación legible del objeto
        return f"Libro: {self.__titulo} por {self.__autor}, {self.__año_publicacion}, {self.__num_paginas} páginas"
    def __repr__(self): # Sobreescribimos el método __repr__ para devolver una representación más detallada del objeto
        return f"Libro: titulo {self.__titulo}, autor {self.__autor}, año_publicacion {self.__año_publicacion}, num_paginas {self.__num_paginas}"
    def __len__(self): # Sobreescribimos el método __len__ para devolver el número de páginas del libro
        return self.__num_paginas

libro = Libro("Cien Años de Soledad", "Gabriel García Márquez", 1967, 417)
print(str(libro))
print(repr(libro))
print(len(libro))