from fastapi import APIRouter, Depends
from users import depends
from users import schemas
from users import service
from users import models

router = APIRouter()


@router.post("/auth/register/")
async def auth_register(auth_data: schemas.AuthData):
    return service.create_user(auth_data)


@router.post("/auth/login/")
async def auth_login(auth_data: schemas.AuthData):
    return service.login_user(auth_data)


@router.get("/me/")
async def me(user: models.User = Depends(depends.validate_authorization)):
    return user.to_dict(exclude=["hashed_password"])
