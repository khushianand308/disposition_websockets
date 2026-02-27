import asyncio
import websockets
import json

async def test_ws():
    uri = "ws://localhost:8005/ws"
    async with websockets.connect(uri) as websocket:
        print("Connecting to WebSocket...")
        payload = {
            "transcript": "Hello, I will pay 500 dollars tomorrow",
            "current_date": "2026-02-27"
        }
        await websocket.send(json.dumps(payload))
        print(f"Sent: {payload}")
        
        response = await websocket.recv()
        print(f"Received: {json.loads(response)}")

if __name__ == "__main__":
    asyncio.run(test_ws())
