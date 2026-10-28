from unittest import TestCase
from pedidos import ProcesadorPedidos
from inventario import Inventario

class TestIntegracion(TestCase):
    def test_flujo_completo(self):
        inventario = Inventario()
        procesador = ProcesadorPedidos(inventario)

        self.assertTrue(procesador.procesar_pedido("producto1", 3))
        self.assertEqual(inventario.productos["producto1"], 7)
        self.assertFalse(procesador.procesar_pedido("producto2", 10))
        self.assertEqual(inventario.productos["producto2"], 5)

if __name__ == "__main__":
    import unittest
    unittest.main()