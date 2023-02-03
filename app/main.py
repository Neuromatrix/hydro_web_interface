from fastapi import FastAPI, WebSocket
from fastapi.responses import HTMLResponse
import src.listener
app = FastAPI()
import time



@app.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        data = src.listener.listener()
        await websocket.send_json(
            {
                "course": data[0],
                "depth": data[1],
                "march": data[2],
                "lag": data[3],
                "roll": data[4],
                "differential": data[5],
                "dropper": data[6],
                "lifter": data[7],
                "global_mission": data[8],
                "local_mission": data[9],
                "transtion": data[10]
            }
        )
        time.sleep(1)

