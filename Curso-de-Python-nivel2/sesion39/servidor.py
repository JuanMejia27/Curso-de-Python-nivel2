import asyncio
from aiohttp import web

clientes = []

async def manejar_conexion(request):
    ws = web.WebSocketResponse()
    await ws.prepare(request)

    clientes.append(ws)
    print("Nuevo cliente concetado")
#Comprueba la conexion para los clientes
    try:
        async for msg in ws:
            if msg.type==web.WSMsgType.TEXT:
                print(f"Mensaje recibido: {msg.data}")
                for cliente in clientes:
                    if cliente != ws:
                        await cliente.send_str(msg.data)
                    elif msg.type == web.WSMsgType.ERROR:
                        print(f"Error de conexion: {ws.exception()}")
    finally:
        clientes.remove(ws)
        print("Cliente desconectado")

    return ws

app = web.Application()
app.router.add_get("/chat", manejar_conexion)
web.run_app(app, host="localhost", port=8080)