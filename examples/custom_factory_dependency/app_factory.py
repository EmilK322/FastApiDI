from fastapi import FastAPI

import endpoints
from deps.abc import Abstract
from deps.impl import Implementation
from FastApiDI.dependency_registry import FastApiDependencyRegistry
from FastApiDI.factory_builders import FactoryBuilder


def custom_factory() -> Abstract:
    print('from custom factory')
    return Implementation()


def create_app() -> FastAPI:
    factory_builder = FactoryBuilder()
    fastapi_dependency_registry = FastApiDependencyRegistry(factory_builder)

    fastapi_dependency_registry.register_factory(Abstract, custom_factory)

    app = FastAPI()
    app.include_router(endpoints.router)
    app.dependency_overrides = fastapi_dependency_registry.to_dependency_overrides()
    return app
