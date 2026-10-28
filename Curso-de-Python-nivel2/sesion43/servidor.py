#MOCKING Y PRUEBAS DE INTEGRACIÓN
import requests #Instalar 

def obtener_datos(url):
    respuesta = requests.get(url)
    if respuesta.status_code == 200:
        return respuesta.json()
    else:
        raise Exception("Error al obtener los datos")