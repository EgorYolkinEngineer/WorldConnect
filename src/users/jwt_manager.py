import datetime

from users.config import JWT, SECRET_KEY
from users.schemas import JWTPair
import jwt


def create_payload(payload: dict, token_type: str) -> dict:
    exp = JWT.get("ACCESS_EXP") if token_type == "access" else JWT.get("REFRESH_EXP")
    payload["exp"] = datetime.datetime.utcnow() + datetime.timedelta(hours=exp)
    return payload


def create_jwt(payload: dict, token_type: str) -> bytes:
    return jwt.encode(create_payload(payload, token_type), SECRET_KEY, algorithm=JWT.get("ALGORITHMS")[0])


def decode_jwt(encode_jwt: str) -> dict:
    return jwt.decode(encode_jwt, "secret", algorithms=JWT.ALGORITHMS)


def create_jwt_pair(user_id: int):
    payload = {
        "user_id": user_id
    }
    access_token = create_jwt(payload, "access")
    refresh_token = create_jwt(payload, "refresh")

    return JWTPair(
        access_token=access_token,
        refresh_token=refresh_token
    )
