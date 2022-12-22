from fastapi import FastAPI

from . import dependencies, routes


def create_app() -> FastAPI:
    app = FastAPI()

    dependencies.init()
    routes.init(app)

    return app
