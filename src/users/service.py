from fastapi import HTTPException
import sqlalchemy.exc
from database import session
from users.models import User
from users import jwt_manager
from users import exceptions
from users import schemas
from users import utils


def create_user(auth_data: schemas.AuthData):
    try:
        user = User()
        user.username = auth_data.username
        user.hashed_password = utils.password_hashing(auth_data.password)
        session.add(user)
        session.flush()
        user_id = user.id
        session.commit()

        return jwt_manager.create_jwt_pair(user_id)
    except sqlalchemy.exc.IntegrityError:
        session.rollback()
        return HTTPException(
            status_code=400,
            detail=exceptions.user_already_exists
        )


def login_user(auth_data: schemas.AuthData):
    user = session.query(User).filter_by(username=auth_data.username).first()
    if user:
        if utils.password_verification(auth_data.password, user.hashed_password):
            return jwt_manager.create_jwt_pair(user.id)
        else:
            return HTTPException(
                status_code=400,
                detail=exceptions.auth_data_is_not_valid
            )
    else:
        return HTTPException(
            status_code=400,
            detail=exceptions.user_not_found
        )
