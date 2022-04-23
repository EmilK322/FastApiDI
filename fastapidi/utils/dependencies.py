import inspect
from typing import Callable, Any, Type, Dict

from fastapi.dependencies.utils import get_typed_signature
from fastapi.params import Depends

__PROXY_CLASSES_CACHE: Dict[str, Type] = {}


def empty_init(self) -> None:
    pass


def create_parameterless_proxy_class(cls: Type) -> Type:
    global __PROXY_CLASSES_CACHE
    class_name = f'{cls.__name__}ParameterlessProxy'
    base_classes = (cls,)
    class_body = {'__init__': empty_init}
    parameterless_proxy_class = type(class_name, base_classes, class_body)
    parameterless_proxy_class = __PROXY_CLASSES_CACHE.setdefault(class_name, parameterless_proxy_class)
    return parameterless_proxy_class


def callable_has_params(callable_: Callable) -> bool:
    signature: inspect.Signature = get_typed_signature(callable_)
    return bool(signature.parameters)


class ParametrizedDepends(Depends):
    def __init__(self, dependency: Callable[..., Any], *, use_cache: bool = True):
        if callable_has_params(dependency):
            dependency = create_parameterless_proxy_class(dependency)
        super().__init__(dependency=dependency, use_cache=use_cache)
