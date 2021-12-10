from fastapi import Depends, APIRouter

from deps.abc import Abstract

router = APIRouter()

# use_cache makes no difference, singleton dependency is called once for FastApi instance


def foo(a: Abstract = Depends(Abstract)):
    return a


@router.get("/")
async def root(my_dep: Abstract = Depends(Abstract), my_dep_nested: Abstract = Depends(foo)):
    print(my_dep.foo(6))
    print(my_dep_nested.foo(8))
    return {"message": "Hello World"}
