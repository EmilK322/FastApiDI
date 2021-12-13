import abc
import uuid

from FastApiDI.dependency_registry import GenericDependencyRegistry
from FastApiDI.factory_builders import FactoryBuilder


class A(abc.ABC):
    @abc.abstractmethod
    def foo(self, z: int) -> str:
        pass


class B(A):
    def __init__(self):
        print(uuid.uuid4())

    def foo(self, z: int) -> str:
        return str(z+1)


fb = FactoryBuilder()
dr = GenericDependencyRegistry(fb)

dr.register_scoped(A, B)
b_fac = dr.get_dependency_factory(A)
print(b_fac())