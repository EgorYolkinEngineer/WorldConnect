from fastapi import APIRouter, Request
from templates.config import templates

router = APIRouter()


@router.get("/auth/")
async def auth(request: Request):
    return templates.TemplateResponse(
        "auth.html",
        {"request": request}
    )


@router.get("/")
async def chat(request: Request):
    return templates.TemplateResponse(
        "chat.html",
        {"request": request}
    )
