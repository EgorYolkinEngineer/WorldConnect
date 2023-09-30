from fastapi.exceptions import HTTPException
from fastapi import Header
from users.models import User
from database import session
from users import exceptions
from users.config import JWT, SECRET_KEY
import jwt


async def validate_authorization(authorization: str = Header()):
    if authorization is None or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail=exceptions.invalid_auth)
    try:
        payload = jwt.decode(authorization.split("Bearer ")[1], SECRET_KEY,
                             algorithms=JWT.get('ALGORITHMS'))

        user = session.query(User).filter_by(id=payload.get("user_id")).first()

        if not user:
            raise jwt.PyJWTError
        return user
    except jwt.PyJWTError:
        raise HTTPException(
            status_code=401,
            detail=exceptions.invalid_jwt
        )
