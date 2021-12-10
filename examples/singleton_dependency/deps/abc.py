import abc


class Abstract(abc.ABC):
    @abc.abstractmethod
    def foo(self, z: int) -> str:
        pass
