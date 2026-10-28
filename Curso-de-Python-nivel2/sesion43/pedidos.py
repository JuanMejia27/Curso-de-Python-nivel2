from inventario import Inventario

class ProcesadorPedidos:
    def __init__(self, inventario):
        self.inventario = inventario

    def procesar_pedido(self, producto, cantidad):
        return self.inventario.actualizar_stock(producto, cantidad)