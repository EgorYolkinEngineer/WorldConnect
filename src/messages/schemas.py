from pydantic import BaseModel


class Message(BaseModel):
    text: str
    topic_id: int


class Topic(BaseModel):
    name: str
    description: str = "Don't description"
