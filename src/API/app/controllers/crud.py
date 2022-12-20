from ..dependencies import db


async def create(object):
    return db.create(object)["id"]


async def read(filter):
    return db.read(filter)


async def update(filter, object):
    db.update(filter, object)


async def delete(filter):
    db.delete(filter)
