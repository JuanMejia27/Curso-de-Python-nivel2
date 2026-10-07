class Vehiculo:
    def mover(self):
        raise NotImplementedError("El método mover debe ser implementado por las subclases.") # Este método es abstracto y debe ser implementado por las subclases.
    '''def __init__(self, marca, modelo):
        self.marca = marca
        self.modelo = modelo
    def arrancar(self):
        print(f"El vehículo {self.marca} {self.modelo} está arrancando.")
    def mover(self):
        print(f"El vehículo se está moviendo.")
    def detener(self):
        print(f"El vehículo {self.marca} {self.modelo} se ha detenido.")'''

class Coche(Vehiculo):
    '''def __init__(self, marca, modelo, tipo_motor):
        super().__init__(marca, modelo)
        self.tipo_motor = tipo_motor'''
    def mover(self):
        print(f"El coche se  está moviendo.")

class Bicicleta(Vehiculo):
    '''def __init__(self, marca, modelo, tipo_bicicleta):
        super().__init__(marca, modelo)
        self.tipo_bicicleta = tipo_bicicleta'''
    def mover(self):
        print(f"La bicicleta se está moviendo.")
class Avion(Vehiculo):
    def mover(self):
        return "El avión se está moviendo."
        #print(f"El avión {self.marca} {self.modelo} está volando.")
def iniciar_movimiento(vehiculo):
    print(vehiculo.mover())

'''vechiculos = Vehiculo("Genero", "Modelo")
coche = Coche("Toyota", "Corolla", "Gasolina")
bicicleta = Bicicleta("Giant", "Defy", "Carretera")

print(coche.mover())
print(bicicleta.mover())'''

coche = Coche()
bicicleta = Bicicleta()
avion = Avion()

iniciar_movimiento(coche)
iniciar_movimiento(bicicleta)
iniciar_movimiento(avion)

#----------------------------------------------------------------------------------
class Empleado:
    def __init__(self, nombre):
        self.nombre = nombre
    def trabajar(self):
        raise NotImplementedError("El método trabajar debe ser implementado por las subclases.")

class Gerente(Empleado):
    def trabajar(self):
        return f"{self.nombre} está gestionando el equipo."
class Desarrollador(Empleado):
    def trabajar(self):
        return f"{self.nombre} está escribiendo código."

def realizar_trabajo(empleado):
    print(empleado.trabajar())

gerente = Gerente("Jose")
desarrollador = Desarrollador("Maria")
realizar_trabajo(gerente)
realizar_trabajo(desarrollador)

class Animal:
    def hacer_sonido(self):
        raise NotImplementedError("El método hacer_sonido debe ser implementado por las subclases.")
class Perro(Animal):
    def hacer_sonido(self):
        return "Guau!"
class Gato(Animal):
    def hacer_sonido(self):
        return "Miau!"

def sonar_animal(animales):
    for animal in animales:
        print(animal.hacer_sonido())

perro = Perro()
gato = Gato()
sonar_animal([perro, gato])