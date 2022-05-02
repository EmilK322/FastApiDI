from typing import Dict, Type, Any

from fastapi import FastAPI
from fastapi.routing import APIRoute

from fastapidi.dependency_registry import GenericDependencyRegistry
from fastapidi.dependency_registry.abc import TDependency, TImplementation, TImplementationFactory
from fastapidi.factory_builders import FactoryBuilder
from fastapidi.factory_builders.abc import AbstractFactoryBuilder
from fastapidi.utils.dependencies import callable_has_params, create_parameterless_proxy_class


class FastApiDI(GenericDependencyRegistry):
    def __init__(self, app: FastAPI):
        factory_builder: AbstractFactoryBuilder = FactoryBuilder()
        super().__init__(factory_builder)
        app.dependency_overrides = self.dependency_overrides
        app.router.dependency_overrides_provider = self
        for route in app.router.routes:
            if isinstance(route, APIRoute):
                route.dependency_overrides_provider = self

    def register_singleton(self, dependency_type: Type[TDependency], implementation_type: Type[TImplementation],
                           *args: Any, **kwargs: Any) -> None:
        super().register_singleton(dependency_type, implementation_type, *args, **kwargs)
        if callable_has_params(dependency_type):
            parameterless_dependency_type = create_parameterless_proxy_class(dependency_type)
            super().register_singleton(parameterless_dependency_type, implementation_type, *args, **kwargs)

    def register_scoped(self, dependency_type: Type[TDependency], implementation_type: Type[TImplementation],
                        *args: Any, **kwargs: Any) -> None:
        super().register_scoped(dependency_type, implementation_type, *args, **kwargs)
        if callable_has_params(dependency_type):
            parameterless_dependency_type = create_parameterless_proxy_class(dependency_type)
            super().register_scoped(parameterless_dependency_type, implementation_type, *args, **kwargs)

    def register_factory(self, dependency_type: Type[TDependency],
                         implementation_factory: TImplementationFactory) -> None:
        super().register_factory(dependency_type, implementation_factory)
        if callable_has_params(dependency_type):
            parameterless_dependency_type = create_parameterless_proxy_class(dependency_type)
            super().register_factory(parameterless_dependency_type, implementation_factory)

    @property
    def dependency_overrides(self) -> Dict:
        return self._dependency_registry_storage
