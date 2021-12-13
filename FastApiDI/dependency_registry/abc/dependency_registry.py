import abc
from typing import TypeVar, Type, Callable, Any

TDependency = TypeVar('TDependency')
TImplementation = TypeVar('TImplementation')
TImplementationFactory = Callable[..., TImplementation]


class AbstractDependencyRegistry(abc.ABC):
    @abc.abstractmethod
    def register_singleton(self, dependency_type: Type[TDependency], implementation_type: Type[TImplementation],
                           *args: Any, **kwargs: Any) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def register_scoped(self, dependency_type: Type[TDependency], implementation_type: Type[TImplementation],
                        *args: Any, **kwargs: Any) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def register_factory(self, dependency_type: Type[TDependency],
                         implementation_factory: TImplementationFactory) -> None:
        raise NotImplementedError

    @abc.abstractmethod
    def get_dependency_factory(self, dependency_type: Type[TDependency]) -> TImplementationFactory:
        raise NotImplementedError
