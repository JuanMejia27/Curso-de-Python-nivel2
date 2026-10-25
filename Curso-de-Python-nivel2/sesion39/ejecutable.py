import asyncio

#Ejecucion de la tarea con un tiempo de espera para su finalizacion
async def tarea(nombre, tiempo):
    print(f"inicio de la tarea: {nombre}")
    await asyncio.sleep(tiempo) #Uso de la rutina para esperar
    print(f"Fin de la tarea: {nombre}")

#Se ejecutan simultaneamente y finalizan de la misma manera en este caso con el valor desendente
async def main():
    tarea1 = asyncio.create_task(tarea("Tarea 1", 3))
    tarea2 = asyncio.create_task(tarea("Tarea 2", 2))
    tarea3 = asyncio.create_task(tarea("Tarea 3", 1))
    await asyncio.gather(tarea1, tarea2, tarea3)

asyncio.run(main())

#uso de la libreria:
import aiohttp

async def hacer_solicitud(url):
    async with aiohttp.ClientSession() as session:
        async with session.get(url) as respuesta:
            resultado = await respuesta.text()
            print(f"Respuesta de {url}; {resultado[:100]}...")
#Toma la primer solicitud disponible asi que puede salir priemro la 2 y al final la 1
async def main():
    urls =[
        'https://jsonplaceholder.typicode.com/post/1',
        'https://jsonplaceholder.typicode.com/post/2',
        'https://jsonplaceholder.typicode.com/post/3'
    ]

    await asyncio.gather(*(hacer_solicitud(url) for url in urls))
asyncio.run(main())