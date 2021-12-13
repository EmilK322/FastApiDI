from typing import Any

from FastApiDI.factory_builders.abc import AbstractFactoryBuilder, TObject, TCallableOfObject, \
    TFactory


class FactoryBuilder(AbstractFactoryBuilder):
    """
    Class for creating factories of callable objects like functions and classes.
    """

    def create_scoped(self, callable_object: TCallableOfObject, *args: Any, **kwargs: Any) -> TFactory:
        """
        Creates scoped factory of callable_object.
        Scoped factory: factory which returns a different instance on every call
        :param callable_object: Callable object to create factory for
        :param args: args for callable_object
        :param kwargs: kwargs for callable_object
        :return: Scoped factory of callable_object
        """

        def factory() -> TObject:
            return callable_object(*args, **kwargs)

        return factory

    def create_singleton(self, callable_object: TCallableOfObject, *args: Any, **kwargs: Any) -> TFactory:
        """
        Creates singleton factory of callable_object.
        Singleton factory: factory which returns the same instance on every call
        :param callable_object: Callable object to create factory for
        :param args: args for callable_object
        :param kwargs: kwargs for callable_object
        :return: Singleton factory of callable_object
        """
        return_value = None
        already_called = False

        def factory() -> TObject:
            nonlocal return_value, already_called
            if already_called:
                return return_value  # type: ignore[return-value]
            return_value = callable_object(*args, **kwargs)
            already_called = True
            return return_value

        return factory
