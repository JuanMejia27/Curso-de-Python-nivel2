class Persona:
    def __init__(self, nombre, edad):
        self.nombre = nombre
        self.edad = edad

    def saludar(self):
        print(f"Hola, mi nombre es {self.nombre} y tengo {self.edad} años.")

persona = Persona("Juan", 30)
persona.saludar()

class Coche:
    cantidad_de_coches = 0
    def __init__(self, marca):
        self.marca = marca
        Coche.incrementar_coche()
    @classmethod
    def incrementar_coche(cls):
        cls.cantidad_de_coches += 1
        print(f"Cantidad de coches: {cls.cantidad_de_coches}")

coche1 =Coche("Toyota")
coche2 =Coche("Honda")
coche3 =Coche("Ford")

class Calculadora:
    @staticmethod
    def sumar(a, b):
        return a + b
    @staticmethod
    def restar(a, b):
        return a - b

resultado_suma = Calculadora.sumar(5, 3)
resultado_resta = Calculadora.restar(10, 4)
print(f"Resultado de la suma: {resultado_suma}")
print(f"Resultado de la resta: {resultado_resta}")

class Empleado:
    cantidad_empleados = 0
    def __init__(self, nombre, salario):
        self.nombre = nombre
        self.salario = salario
        Empleado.incrementar_empleado()
    @classmethod
    def incrementar_empleado(cls):
        cls.cantidad_empleados += 1
    @staticmethod
    def calcular_bonificacion(salario):
        if salario < 3000:
            return salario * 0.15
        else:
            return salario * 0.10
    @classmethod
    def obtener_total_de_empleados(cls):
        return cls.cantidad_empleados

# Creart empleados
empleado1 = Empleado("Ana", 2500)
empleado2 = Empleado("Luis", 3500)
empleado3 = Empleado("Marta", 2800)

print(f"Total de empleados: {Empleado.obtener_total_de_empleados()}")

bonificacion = Empleado.calcular_bonificacion(empleado1.salario)
print(f"Bonificacion de {empleado1.nombre}: {bonificacion}")

class CuentaBancaria:
    cuentas = 0
    def __init__(self, nombre, saldo = 0):
            self.nombre = nombre
            self.saldo = saldo
            CuentaBancaria.cuentas += 1
    def depositar(self, cantidad):
        self.saldo += cantidad
        print(f"Depósito de {cantidad}. Nuevo saldo: {self.saldo}")
    def retirar(self, cantidad):
        if CuentaBancaria.validar_transaccion(self.saldo, cantidad):
            self.saldo -= cantidad
            print(f"Retiro de {cantidad}. Nuevo saldo: {self.saldo}")
    @classmethod
    def cuentas_abiertas(cls):
        return cls.cuentas
    @staticmethod
    def validar_transaccion(saldo, cantidad):
        if cantidad > saldo:
            print("Fondos insuficientes.")
            return False
        return True

cliente1 = CuentaBancaria("Carlos", 1800)
cliente1.depositar(500)
cliente1.retirar(1000)