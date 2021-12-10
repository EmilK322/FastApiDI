from copy import deepcopy
from typing import Dict

from fastapi_di.dependency_registry.abc import TDependency, TImplementationFactory
from fastapi_di.dependency_registry.generic_dependency_registry import GenericDependencyRegistry
from fastapi_di.factory_builders.abc import AbstractFactoryBuilder


class FastApiDependencyRegistry(GenericDependencyRegistry):
    def __init__(self, factory_builder: AbstractFactoryBuilder) -> None:
        super().__init__(factory_builder)

    def to_dependency_overrides(self) -> Dict[TDependency, TImplementationFactory]:
        return deepcopy(self._dependency_registry_storage)
