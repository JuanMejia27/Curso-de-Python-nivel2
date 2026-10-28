from unittest import TestCase
from unittest.mock import patch
from servidor import obtener_datos

class TestServicio(TestCase):
    @patch('servidor.requests.get')
    def tets_obtener_datos_exito(self, mock_get):
        mock_get.return_value.status_code = 200
        mock_get.return_value.json.return_value = {"clave":"valor"}
        resultado = obtener_datos("http://example.com")
        self.assertEqual(resultado, {"clave":"valor"})

    @patch('servidor.requests.get')
    def tets_obtener_datos_error(self, mock_get):
        mock_get.return_value.status_code = 500
        with self.assertRaises(Exception):
            obtener_datos("http://example.com")
#corremos la prueba del servicio con: python -m unittest test_servicio/nombre_del_archivo

#