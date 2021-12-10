from fastapi import Depends, APIRouter

from deps.abc import Abstract


router = APIRouter()

# custom factory behaves based on the logic of the factory,
# if use_cache is True, it is probably that Depends will call it for each route request,
# but there is no predefined logic


def foo(a: Abstract = Depends(Abstract)):
    return a


@router.get("/")
async def root(my_dep: Abstract = Depends(Abstract), my_dep_nested: Abstract = Depends(foo)):
    print(my_dep.foo(6))
    print(my_dep_nested.foo(8))
    return {"message": "Hello World"}
