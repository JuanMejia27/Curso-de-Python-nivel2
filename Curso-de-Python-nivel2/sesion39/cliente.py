import asyncio
import websockets

#Conexion inicial
async def enviar_mensaje():
    uri = "ws://localhost:8080/chat"
    async with websockets.connect(uri) as websocket:
        while True:
            mensaje = input("Escribe un mensaje: ")
            await websocket.send(mensaje)

asyncio.run(enviar_mensaje())