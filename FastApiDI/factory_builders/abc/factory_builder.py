import abc
from typing import TypeVar, Callable, Any

TObject = TypeVar('TObject')
TCallableOfObject = Callable[..., TObject]
TFactory = Callable[[], TObject]


class AbstractFactoryBuilder(abc.ABC):
    """
    Interface for creating factories of callable objects like functions and classes.
    """

    @abc.abstractmethod
    def create_scoped(self, callable_object: TCallableOfObject, *args: Any, **kwargs: Any) -> TFactory:
        """
        Creates scoped factory of callable_object.
        Scoped factory: factory which returns a different instance on every call
        :param callable_object: Callable object to create factory for
        :param args: args for callable_object
        :param kwargs: kwargs for callable_object
        :return: Scoped factory of callable_object
        """
        raise NotImplementedError

    @abc.abstractmethod
    def create_singleton(self, callable_object: TCallableOfObject, *args: Any, **kwargs: Any) -> TFactory:
        """
        Creates singleton factory of callable_object.
        Singleton factory: factory which returns the same instance on every call
        :param callable_object: Callable object to create factory for
        :param args: args for callable_object
        :param kwargs: kwargs for callable_object
        :return: Singleton factory of callable_object
        """
        raise NotImplementedError
