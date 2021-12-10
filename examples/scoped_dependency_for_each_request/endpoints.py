from fastapi import Depends, APIRouter

from deps.abc import Abstract

router = APIRouter()

# because of use_cache=True, the Depends will call for the scoped dependency on each route request
# and cache it for that request


def foo(a: Abstract = Depends(Abstract)):
    return a


@router.get("/")
async def root(my_dep: Abstract = Depends(Abstract), my_dep_nested: Abstract = Depends(foo)):
    print(my_dep.foo(6))
    print(my_dep_nested.foo(8))
    return {"message": "Hello World"}
