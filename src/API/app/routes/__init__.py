from .crud import router as crud_router
from .process import router as process_router


def init(app):
    app.include_router(crud_router)
    app.include_router(process_router)
