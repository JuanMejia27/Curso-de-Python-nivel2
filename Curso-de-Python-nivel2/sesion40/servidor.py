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

'''import asyncio
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

web.run_app(app, host='localhost', port=8080)'''

'''import asyncio

async def tarea(id, duracion):
    print(f"Tarea {id} comenzando")
    await asyncio.sleep(duracion)
    print(f"Tarea {id} terminada")

async def main():
    tareas = [tarea(1,2), tarea(2,3), tarea(3,1)]
    await asyncio.gather(*tareas)

asyncio.run(main())'''

'''from multiprocessing import Pool
import time

def calcular_cuadrado(x):
    time.sleep(1)
    return x*x

if __name__ == "__main__":
    datos = [1,2,3,4,5]
    with Pool(processes=3) as pool:
        resultados = pool.map(calcular_cuadrado,datos)
        print("Resultados: ", resultados)'''

import asyncio
from multiprocessing import Pool
import random, time

def obtener_recomendacion(usuario_id):
    time.sleep(1)
    recomendaciones = [f"Recomencacion {i}" for i in range(5)]
    return f"usuario {usuario_id}: {random.choice(recomendaciones)}"

async def manejar_solicitud(usuario_id):
    print(f"Procesando usuario {usuario_id} de forma concurrente...")
    recomendacion = await asyncio.to_thread(obtener_recomendacion, usuario_id)
    print(f"Resultado para usuario {usuario_id}: {recomendacion}")

async def main_concurrente():
    usuarios = [1,2,3,4,5]
    tareas = [manejar_solicitud(usuario) for usuario in usuarios]
    await asyncio.gather(*tareas)


def main_paralelo():
    usuarios = [1,2,3,4,5]
    with Pool(processes=3) as pool:
        resultados = pool.map(obtener_recomendacion, usuarios)
        for resultado in resultados:
            print("Resultado paralelo: ", resultado)

if __name__ == "__main__":
    print("Ejecutando sistema de recomendacion concurrente...")
    asyncio.run(main_concurrente())
    print("\nEjecutando sistema de recomendacion paralelo")
    main_paralelo()