from fastapi import FastAPI

import endpoints
from deps import ParametrizedClass
from fastapidi.facades import FastApiDI


def create_app() -> FastAPI:
    app = FastAPI()
    app_di = FastApiDI(app)

    register_dependencies(app_di)
    register_routers(app)

    return app


def register_dependencies(app_di: FastApiDI):
    app_di.register_scoped(ParametrizedClass, ParametrizedClass, first_param=6)


def register_routers(app: FastAPI):
    app.include_router(endpoints.router)
