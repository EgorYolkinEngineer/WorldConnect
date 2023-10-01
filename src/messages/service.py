from fastapi import HTTPException
from database import session
from sqlalchemy import or_
from users import models as users_models
from messages import models
from messages import schemas
from messages import exceptions


def create_message(message: schemas.Message, user: users_models.User) -> dict:
    message = models.Message(
        text=message.text,
        topic_id=message.topic_id,
        user_id=user.id
    )
    session.add(message)
    session.flush()
    message = message.to_dict()
    session.commit()

    return message


def delete_message(message_id: int, user: users_models.User):
    message = session.query(models.Message).filter_by(id=message_id,
                                                      user_id=user.id).first()
    if message:
        session.delete(message)
        session.commit()
    else:
        return HTTPException(
            status_code=400,
            detail=exceptions.message_not_found
        )


def get_user(user_id: int) -> users_models.User:
    return session.query(users_models.User).filter_by(id=user_id).first()


def topic_create(topic: schemas.Topic, user: users_models.User) -> dict:
    topic = models.Topic(
        name=topic.name,
        description=topic.description,
        creator_id=user.id
    )
    session.add(topic)
    session.flush()
    topic = topic.to_dict()
    session.commit()

    return topic


def get_topic_history(topic_id: int, offset: int, limit: int) -> list[dict]:
    limit = 50 if limit > 50 else limit
    chat_history_queryset = session.query(models.Message).filter_by(topic_id=topic_id).offset(offset).limit(limit).all()
    chat_history_queryset = [_.to_dict() for _ in chat_history_queryset]

    for _ in chat_history_queryset:
        _["user"] = get_user(_["user_id"]).to_dict()
        _.pop("user_id")

    return chat_history_queryset


def get_topics_list(q: str, offset: int, limit: int) -> list[dict]:
    limit = 15 if limit > 15 else limit
    print(q)
    if q:
        topics_queryset = session.query(models.Topic).filter(or_(models.Topic.name.icontains(q),
                                                                 models.Topic.description.icontains(q))
                                                             ).offset(offset).limit(limit).all()
    else:
        topics_queryset = session.query(models.Topic).offset(offset).limit(limit).all()

    topics_queryset_list = []
    for topic in topics_queryset:
        data = topic.to_dict()
        data['messages_count'] = session.query(models.Message).filter_by(
            topic_id=topic.id
        ).count()
        topics_queryset_list.append(data)

    return topics_queryset_list
