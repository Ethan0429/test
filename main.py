import os
import asyncio
from websockets.server import serve


async def echo(websocket):
    async for message in websocket:
        try:
            await websocket.send(message)
        except Exception as e:
            print(e)
        print(f"received: {message}")


async def main():
    port = os.getenv("PORT", "3000")
    async with serve(echo, "0.0.0.0", port):
        print(f"running websocket server on port {port}")
        await asyncio.Future()  # run forever

asyncio.run(main())
