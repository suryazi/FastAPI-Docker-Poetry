import uvicorn
from api.app.routers import default
from api.core.config import settings
from fastapi import FastAPI


def include_router(app):
    app.include_router(default.router)


def start_application():
    app = FastAPI(title=settings.APP_TITLE, version=settings.APP_VERSION)
    include_router(app)
    return app


if __name__ == "__main__":
    app = start_application()
    uvicorn.run(app, host=settings.APP_HOST, port=int(settings.APP_PORT))
