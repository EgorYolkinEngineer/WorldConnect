from fastapi import APIRouter, Depends
from users import depends as user_depends
from users.models import User
from messages import schemas
from messages import service

router = APIRouter()


@router.post("/send")
async def send(message: schemas.Message, user: User = Depends(user_depends.validate_authorization)):
    return service.create_message(message, user)


@router.post("/delete")
async def delete(message_id: int, user: User = Depends(user_depends.validate_authorization)):
    return service.delete_message(message_id, user)


@router.post('/topics/create')
async def topics_create(topic: schemas.Topic, user: User = Depends(user_depends.validate_authorization)):
    return service.topic_create(topic, user)


@router.post("/topics/{topic_id}/history")
async def topic_history(topic_id: int, offset: int = 0, limit: int = 50,
                        user: User = Depends(user_depends.validate_authorization)):
    return service.get_topic_history(topic_id, offset, limit)


@router.get('/topics/list')
async def topics_list(q: str = None, offset: int = 0, limit: int = 50):
    return service.get_topics_list(q, offset, limit)
