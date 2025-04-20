import asyncio
from aiohttp import web, ClientSession, WSMsgType

BACKEND_SERVERS = [
    'http://localhost:8081',
    'http://localhost:8082'
]
WS_BACKEND_PATH = '/ws'  # the path to forward WebSocket requests to
server_index = 0
lock = asyncio.Lock()

async def get_backend_url():
    global server_index
    async with lock:
        url = BACKEND_SERVERS[server_index]
        server_index = (server_index + 1) % len(BACKEND_SERVERS)
        return url

# WebSocket reverse proxy
async def websocket_proxy_handler(request):
    backend_url = await get_backend_url()
    full_ws_url = backend_url.replace('http', 'ws') + WS_BACKEND_PATH

    ws_server = web.WebSocketResponse()
    await ws_server.prepare(request)

    async with ClientSession() as session:
        async with session.ws_connect(full_ws_url) as ws_client:

            async def client_to_server():
                async for msg in ws_server:
                    if msg.type == WSMsgType.TEXT:
                        await ws_client.send_str(msg.data)
                    elif msg.type == WSMsgType.BINARY:
                        await ws_client.send_bytes(msg.data)
                    elif msg.type == WSMsgType.CLOSE:
                        await ws_client.close()

            async def server_to_client():
                async for msg in ws_client:
                    if msg.type == WSMsgType.TEXT:
                        await ws_server.send_str(msg.data)
                    elif msg.type == WSMsgType.BINARY:
                        await ws_server.send_bytes(msg.data)
                    elif msg.type == WSMsgType.CLOSE:
                        await ws_server.close()

            await asyncio.gather(client_to_server(), server_to_client())

    return ws_server

# Streaming HTTP proxy
async def http_proxy_handler(request):
    backend_url = await get_backend_url()
    full_url = backend_url + request.rel_url.path_qs

    async with ClientSession() as session:
        async with session.request(
            method=request.method,
            url=full_url,
            headers={k: v for k, v in request.headers.items() if k.lower() != 'host'},
            data=request.content.iter_any()
        ) as resp:

            stream_resp = web.StreamResponse(status=resp.status)
            for k, v in resp.headers.items():
                if k.lower() != 'transfer-encoding':
                    stream_resp.headers[k] = v

            await stream_resp.prepare(request)

            async for chunk in resp.content.iter_chunked(4096):
                await stream_resp.write(chunk)

            await stream_resp.write_eof()
            return stream_resp

# Route dispatcher
async def dispatcher(request):
    if request.headers.get('Upgrade', '').lower() == 'websocket':
        return await websocket_proxy_handler(request)
    else:
        return await http_proxy_handler(request)

app = web.Application()
app.router.add_route('*', '/{tail:.*}', dispatcher)

if __name__ == '__main__':
    web.run_app(app, port=8080)
    

import os
from flask_script import Manager

from app import create_app, db
from commands.seed_command import SeedCommand

env = os.getenv("FLASK_ENV") or "test"
print(f"Active environment: * {env} *")
app = create_app(env)

manager = Manager(app)
app.app_context().push()
manager.add_command("seed_db", SeedCommand)


@manager.command
def run():
    app.run()


@manager.command
def init_db():
    print("Creating all resources.")
    db.create_all()


@manager.command
def drop_all():
    if input("Are you sure you want to drop all tables? (y/N)\n").lower() == "y":
        print("Dropping tables...")
        db.drop_all()


if __name__ == "__main__":
    manager.run()
