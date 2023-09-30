from fastapi import APIRouter

router = APIRouter()


@router.get('/get/')
async def test_get(param: str):
    return {
        'data': param
    }
