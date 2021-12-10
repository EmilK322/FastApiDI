from fastapi import Depends, APIRouter

from deps.abc import Abstract

router = APIRouter()

# because of use_cache=False, the Depends will call for the scoped dependency each time it is depends on


def foo(a: Abstract = Depends(Abstract, use_cache=False)):
    return a


@router.get("/")
async def root(my_dep: Abstract = Depends(Abstract, use_cache=False), my_dep_nested: Abstract = Depends(foo, use_cache=False)):
    print(my_dep.foo(6))
    print(my_dep_nested.foo(8))
    return {"message": "Hello World"}
