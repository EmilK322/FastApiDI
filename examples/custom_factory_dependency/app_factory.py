from fastapi import FastAPI

import endpoints
from deps.abc import Abstract
from deps.impl import Implementation
from fastapidi.facades import FastApiDI


def custom_factory() -> Abstract:
    print('from custom factory')
    return Implementation()


def create_app() -> FastAPI:
    app = FastAPI()
    app_di = FastApiDI(app)

    register_dependencies(app_di)
    register_routers(app)

    return app


def register_dependencies(app_di: FastApiDI):
    app_di.register_factory(Abstract, custom_factory)


def register_routers(app: FastAPI):
    app.include_router(endpoints.router)
