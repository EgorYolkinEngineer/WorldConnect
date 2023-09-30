from fastapi import APIRouter, Depends
from users import depends as user_depends
from users.models import User
from messages import schemas
from messages import service

router = APIRouter()


@router.post("/send/")
async def send(message: schemas.Message, user: User = Depends(user_depends.validate_authorization)):
    return service.create_message(message, user)


@router.post("/chat/history/",
             description="Get chat history with offset && limit")
async def send(offset: int = 0, limit: int = 50,
               user: User = Depends(user_depends.validate_authorization)):
    return service.get_chat_history(offset, limit)
