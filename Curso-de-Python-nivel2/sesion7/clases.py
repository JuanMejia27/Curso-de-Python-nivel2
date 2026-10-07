from abc import ABC, abstractclassmethod, abstractmethod, ABCMeta #importamos ABC y abstractclassmethod para crear clases abstractas


class FiguraGeometrica(ABC):
    @abstractclassmethod
    def area(self):
        pass

class Circulo(FiguraGeometrica):
    def __init__(self, radio):
        self.radio = radio
    def area(self):
        return 3.14 * self.radio ** 2

class Rectangulo(FiguraGeometrica):
    def __init__(self, base, altura):
        self.base = base
        self.altura = altura
    def area(self):
        return self.base * self.altura

circulo = Circulo(7)
rectangulo =  Rectangulo(5, 10)

print(circulo.area())
print(rectangulo.area())

class Empleado(ABC):
    @abstractmethod
    def trabajar(self):
        pass 
    @abstractmethod
    def descansar(self):
        pass

class Gerente(Empleado):
    def trabajar(self):
        return "El gerente está gestionando el equipo"
    def descansar(self):
        return "El gerente está descansando"

class Desarrollador(Empleado):
    def trabajar(self):
        return "El desarrollador está escribiendo código"
    def descansar(self):
        return "Tomando un descanso de la computadora"

gerente = Gerente()
desarrollador = Desarrollador()

print(gerente.trabajar())
print(gerente.descansar())
print(desarrollador.trabajar())
print(desarrollador.descansar())

class Volador(ABC):
    @abstractmethod
    def volar(self):
        pass

class Ave(Volador):
    def volar(self):
        return "El ave esta volando"

class Avion(Volador):
    def volar(self):
        return "El avión está volando"

ave = Ave()
avion = Avion()

print(ave.volar())
print(avion.volar())

class Animal(metaclass=ABCMeta):
    @abstractmethod
    def hacer_sonido(self):
        pass

class Perro(Animal):
    def hacer_sonido(self):
        return "Guau"

perro = Perro()
print(perro.hacer_sonido())
#animal = Animal()  # Esto generará un error, ya que no se puede instanciar una clase abstracta