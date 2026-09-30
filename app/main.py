from fastapi import FastAPI
from app.routers import websocket

app = FastAPI()
app.include_router(websocket.router)

@app.get("/")
async def root():
    return{"message": "System running"}