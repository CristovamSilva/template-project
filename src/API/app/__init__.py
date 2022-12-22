from . import dependencies, routes
from fastapi import FastAPI



def create_app() -> FastAPI:
    app = FastAPI()

    dependencies.init()
    routes.init(app)

    return app
