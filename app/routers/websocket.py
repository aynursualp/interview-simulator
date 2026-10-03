from fastapi import APIRouter, WebSocket, WebSocketDisconnect
import base64
import numpy as np
import cv2
from  app.services.cv_analyzer import CVAnalyzer

router = APIRouter()
cv_analyzer = CVAnalyzer()

@router.websocket("/ws")
async def websocket_endpoint(websocket: WebSocket):
    await websocket.accept()
    while True:
        try:
            data = await websocket.receive_text()
            pure_data = data.split(",")[1]

            byte_data = base64.b64decode(pure_data)
            np_arr = np.frombuffer(byte_data, dtype=np.uint8)
            img = cv2.imdecode(np_arr, cv2.IMREAD_COLOR)

            if img is not None:
                analysis_results = cv_analyzer.analyze_frame(img)
                print(analysis_results)
            else:
                print("Error: Could not decode image.")

            #results = cv_analyzer.analyze_frame(img)
           
        except WebSocketDisconnect:
            print("Connection lost")