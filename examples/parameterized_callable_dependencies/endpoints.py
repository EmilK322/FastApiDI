from fastapi import APIRouter

from deps import ParametrizedClass
from fastapidi.utils.dependencies import ParametrizedDepends

router = APIRouter()


@router.get("/")
def root(parametrized_dep: ParametrizedClass = ParametrizedDepends(ParametrizedClass)):
    parametrized_dep.print_param()
    return {"message": "Hello World"}
