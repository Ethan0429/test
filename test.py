# server.py
import asyncio
import websockets
import os


async def echo(websocket, path):
    async for message in websocket:
        print(f"Received message: {message}")

start_server = websockets.serve(
    echo, "0.0.0.0", os.environ.get("PORT", 8765))

asyncio.get_event_loop().run_until_complete(start_server)
asyncio.get_event_loop().run_forever()
