from fastapi import FastAPI

import endpoints
from deps.abc import Abstract
from deps.impl import Implementation
from fastapi_di.dependency_registry import FastApiDependencyRegistry
from fastapi_di.factory_builders import FactoryBuilder


def create_app() -> FastAPI:
    factory_builder = FactoryBuilder()
    fastapi_dependency_registry = FastApiDependencyRegistry(factory_builder)

    fastapi_dependency_registry.register_scoped(Abstract, Implementation)

    app = FastAPI()
    app.include_router(endpoints.router)
    app.dependency_overrides = fastapi_dependency_registry.to_dependency_overrides()
    return app
