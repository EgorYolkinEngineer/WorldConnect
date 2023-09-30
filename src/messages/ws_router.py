from fastapi import APIRouter, Depends
from messages import ws_manager
from users import models as users_models
from users import depends as users_depends
from messages import schemas
from messages import service

router = APIRouter()

manager = ws_manager.ConnectionManager()


@router.websocket("/chat/")
async def websocket_endpoint(websocket: WebSocket,
                             user: users_models.User = Depends(users_depends.validate_authorization)):
    await manager.connect(websocket)
    while True:
        text = await websocket.receive_text()
        message = schemas.Message(text=text)
        service.create_message(message, user)
        await manager.broadcast(text)
