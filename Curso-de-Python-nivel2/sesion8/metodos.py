

class Multiplicador:
    def __init__(self, factor):
        self.factor = factor

    def __call__(self, numero):
        return numero * self.factor 

multiplicar_por_3 = Multiplicador(3)
print(multiplicar_por_3(5))  # Salida: 15

class MiClase:
    def __init__(self):
        print("Objeto creado")
    def __del__(self):
        print("Objeto destruido")
objeto = MiClase()
del objeto  # Esto desencadenará la llamada a __del__ y mostrará "Objeto destruido"

class Contador:
    def __init__(self, limite):
        self.limite = limite
        self.numero = 0
    def __iter__(self):
        return self
    def __next__(self):
        if self.numero >= self.limite:
            raise StopIteration
        self.numero += 1
        return self.numero

contador = Contador(5)
for numero in contador:
    print(numero)  # Salida: 1, 2, 3, 4, 5 o el valor que se cambie según el límite establecido

class Punto:
    def __init__(self, x, y):
        self.x = x
        self.y = y
    def __eq__(self, otro):
        return self.x == otro.x and self.y == otro.y
    def __lt__(self, otro):
        return (self.x**2 + self.y**2) < (otro.x**2 + otro.y**2)

punto1 = Punto(2, 3)
punto2 = Punto(2, 3)
punto3 = Punto(1, 1)

print(punto1 == punto2)
print(punto1 < punto2)
print(punto3 < punto1)

# Uso de multiples metodos
class Producto:
    def __init__(self, nombre, precio, cantidad):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
    def __repr__(self):
        return f"Producto(nombre={self.nombre}, precio={self.precio}, cantidad={self.cantidad})"
    def __eq__(self, otro):
        return self.nombre == otro.nombre
    def __lt__(self, other):
        return self.precio < other.precio

class inventario:
    def __init__(self):
        self.productos = {}
    def __getitem__(self, nombre):
        return self.productos.get(nombre, "Producto no encontrado")
    def __setitem__(self, nombre, producto):
        self.productos[nombre] = producto
    def __delitem__(self, nombre):
        if nombre in self.productos:
            del self.productos[nombre]
        else:
            print("Producto no encontrado para eliminar")
    def __iter__(self):
        self.productos_iter = iter(self.productos.values())
        return self
    def __next__(self):
        return next(self.productos_iter)
    def __call__(self, nombre):
        return self.__getitem__(nombre)
    def valor_total(self):
        return sum(p.precio * p.cantidad for p in self.productos.values())

p1 = Producto("Laptop", 1000, 5)
p2 = Producto("Mouse", 25, 10)
p3 = Producto("Teclado", 100, 5)

inventario = inventario()
inventario["Laptop"] = p1
inventario["Mouse"] = p2
inventario["Teclado"] = p3

print(inventario["Laptop"])
print(inventario.valor_total())

inventario["Laptop"] = Producto("Laptop", 1800, 7)

print(inventario["Laptop"])

del inventario["Mouse"]

for producto in inventario: 
    print(producto)

print(inventario("Teclado"))  # Llamada al método __call__ para obtener el producto "Teclado"
print("Valor total del inventario:", inventario.valor_total()) # Valor total del inventario