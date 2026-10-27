'''import unittest #uso de pruebas con unitest
from calculadora import Calculadora

class TestCalculadora(unittest.TestCase):
    def setUp(self):
        self.calc = Calculadora()

    def test_sumar(self):
        self.assertEqual(self.calc.sumar(2,3),5)
        self.assertEqual(self.calc.sumar(-2,2),0)

    def test_dividir(self):
        self.assertEqual(self.calc.dividir(10,2),5)
        with self.assertRaises(ValueError):
            self.calc.dividir(10,0)

if __name__ == '__main__':
    unittest.main()'''

#Uso de pytest para pruebas, se usa pytest y el nombre del archivo
import pytest
from calculadora import Calculadora

@pytest.fixture
def calculadora():
    return Calculadora()

def test_sumar(calculadora):
    assert calculadora.sumar(2,3)==5
    assert calculadora.sumar(-2,2)==0

def test_dividir(calculadora):
    assert calculadora.dividir(10,2)==5
    assert calculadora.dividir(8,2)==4
    with pytest.raises(ValueError):
        calculadora.dividir(10,0)

def test_restar(calculadora):
    assert calculadora.restar(2, 3) == -1
    assert calculadora.restar(-1, 1) == -2
    assert calculadora.restar(5, 3) == 2
    assert calculadora.restar(0, 3) == -3

def test_multiplicar(calculadora):
    assert calculadora.multiplicar(2, 3) == 6
    assert calculadora.multiplicar(-1, 1) == -1
    assert calculadora.multiplicar(0, 5) == 0

@pytest.mark.parametrize("a, b, resultado", [(2,3,5),(-1,1,0),(0,0,0)])
def test_sumar_parametrizado(calculadora, a, b, resultado):
    assert calculadora.sumar(a, b) == resultado