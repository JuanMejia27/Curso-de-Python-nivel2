import asyncio
import aiohttp

async def hacer_peticion():
    url = 'http://localhost:8080/obtener_datos'
    async with aiohttp.ClientSesion() as session:
        async with session.get(url) as response:
            texto = await response.text()
            print(texto)

asyncio.run(hacer_peticion())