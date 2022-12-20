from http import HTTPStatus

from fastapi import APIRouter

from ..controllers.crud import create, delete, read, update

router = APIRouter(prefix="/database")


@router.post("/create", status_code=HTTPStatus.CREATED)
async def register(object):
    oid = await create(object)
    return {"id": oid}


@router.get("/read", status_code=HTTPStatus.OK)
async def fetch(filter):
    obj = await read(filter)
    return {"message": obj}


@router.post("/update", status_code=HTTPStatus.OK)
async def change(filter, object):
    await update(filter, object)
    return {"message": "updated"}


@router.post("/delete", status_code=HTTPStatus.NO_CONTENT)
async def remove(filter):
    await delete(filter)
    return {"message": "deleted"}
