from typing import Dict

from fastapi import FastAPI

from fastapidi.dependency_registry import GenericDependencyRegistry
from fastapidi.factory_builders import FactoryBuilder
from fastapidi.factory_builders.abc import AbstractFactoryBuilder


class FastApiDI(GenericDependencyRegistry):
    def __init__(self, app: FastAPI):
        factory_builder: AbstractFactoryBuilder = FactoryBuilder()
        super().__init__(factory_builder)
        app.router.dependency_overrides_provider = self

    @property
    def dependency_overrides(self) -> Dict:
        return self._dependency_registry_storage
