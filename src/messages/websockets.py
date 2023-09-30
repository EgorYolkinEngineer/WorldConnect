from fastapi import APIRouter, WebSocket, Depends
from users import models as users_models
from users import depends as users_depends
from messages import schemas
from messages import service

router = APIRouter()


class ConnectionManager:
    def __init__(self):
        self.active_connections: list[WebSocket] = []

    async def connect(self, websocket: WebSocket):
        await websocket.accept()
        self.active_connections.append(websocket)

    def disconnect(self, websocket: WebSocket):
        self.active_connections.remove(websocket)

    async def broadcast(self, message: str):
        for connection in self.active_connections:
            await connection.send_text(message)


manager = ConnectionManager()


@router.websocket("/chat/")
async def websocket_endpoint(websocket: WebSocket,
                             user: users_models.User = Depends(users_depends.validate_authorization)):
    await manager.connect(websocket)
    while True:
        text = await websocket.receive_text()
        message = schemas.Message(text=text)
        service.create_message(message, user)
        await manager.broadcast(text)
