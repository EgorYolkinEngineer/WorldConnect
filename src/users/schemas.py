from pydantic import BaseModel


class AuthData(BaseModel):
    username: str
    password: str


class JWTPair(BaseModel):
    access_token: bytes
    refresh_token: bytes
