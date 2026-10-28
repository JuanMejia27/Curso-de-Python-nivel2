class Inventario:
    def __init__(self):
        self.productos = {"producto1": 10, "producto2": 5}

    def actualizar_stock(self, producto, cantidad):
        if producto in self.productos and self.productos[producto] >= cantidad:
            self.productos[producto] -= cantidad
            return True
        return False