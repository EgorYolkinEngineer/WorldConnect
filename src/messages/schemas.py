from pydantic import BaseModel


class Message(BaseModel):
    text: str
    topic_id: int


class ResponseMessage(BaseModel):
    ...
