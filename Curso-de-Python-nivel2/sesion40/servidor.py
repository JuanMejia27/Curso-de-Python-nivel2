'''import time
#Leectura de un archivo ya existente
def leer_archivo():
    with open('archivo.txt', 'r') as archivo:
        contenido = archivo.read()
        time.sleep(2)
    return contenido

contenido = leer_archivo()
print("Archivo leido", contenido)'''

'''import asyncio
async def obtener_datos(url):
    print(f"Comenzando a obtener datos de {url}")
    await asyncio.sleep(2)
    print(f"Datos obtenidos de {url}")

async def main():
    tareas = [obtener_datos(f"https://example.com/{i}") for i in range(3)] #Lo ejecuta 3 veces o segun el valor en rango
    await asyncio.gather(*tareas)

asyncio.run(main())'''

'''import asyncio
import aiohttp

async def hacer_solicitud(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as respuesta:
            datos = await respuesta.text()
            print(f"Respuesta de {url}: {datos[:100]}")
#Al ajecutar es el primero en iniciar asi que puede ser en cualquier orden, como en peticiones a una pagina web
async def main():
    urls = [
        'https://jsonplaceholder.typicode.com/post/1',
        'https://jsonplaceholder.typicode.com/post/2',
        'https://jsonplaceholder.typicode.com/post/3'
    ]
    tareas = [hacer_solicitud(url) for url in urls]
    await asyncio.gather(*tareas)

asyncio.run(main())'''

import asyncio
from aiohttp import web
import aiohttp
import os 

async def descargar_pagina(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as response:
            datos = await response.text()

async def leer_archivo(path):
    await asyncio.sleep(2)
    with open(path, 'r') as f:
        return f.read()

async def manejar_peticion(request):
    archivo_path = 'archivo.txt'
    contenido_archivo = await leer_archivo(archivo_path)

    url = 'https://example.com'
    pagina = await descargar_pagina(url)

    return web.Response(text=f"Contenido del archivo: \n{contenido_archivo}\n\nPagina descargada\n{pagina}")

app = web.Application()
app.router.add_get('/obtener_datos', manejar_peticion)

web.run_app(app, host='localhost', port=8080)