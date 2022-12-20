from http import HTTPStatus

from fastapi import APIRouter

from ..controllers.process import run

router = APIRouter(prefix="/process")


@router.post("", status_code=HTTPStatus.OK)
async def process():
    await run()
    return {"message": "ok"}
