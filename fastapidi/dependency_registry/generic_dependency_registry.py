from typing import Type, Dict, Any

from fastapidi.dependency_registry.abc import AbstractDependencyRegistry, TDependency, \
    TImplementation, TImplementationFactory
from fastapidi.factory_builders.abc import AbstractFactoryBuilder


class GenericDependencyRegistry(AbstractDependencyRegistry):
    def __init__(self, factory_builder: AbstractFactoryBuilder) -> None:
        self._factory_builder = factory_builder
        self._dependency_registry_storage: Dict = dict()

    def register_singleton(self, dependency_type: Type[TDependency], implementation_type: Type[TImplementation],
                           *args: Any, **kwargs: Any) -> None:
        implementation_factory = self._factory_builder.create_singleton(implementation_type, *args, **kwargs)
        self._dependency_registry_storage[dependency_type] = implementation_factory

    def register_scoped(self, dependency_type: Type[TDependency], implementation_type: Type[TImplementation],
                        *args: Any, **kwargs: Any) -> None:
        implementation_factory = self._factory_builder.create_scoped(implementation_type, *args, **kwargs)
        self._dependency_registry_storage[dependency_type] = implementation_factory

    def register_factory(self, dependency_type: Type[TDependency],
                         implementation_factory: TImplementationFactory) -> None:
        self._dependency_registry_storage[dependency_type] = implementation_factory

    def get_dependency_factory(self, dependency_type: Type[TDependency]) -> TImplementationFactory:
        return self._dependency_registry_storage[dependency_type]
