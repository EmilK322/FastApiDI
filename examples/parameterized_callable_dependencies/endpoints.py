from fastapi import APIRouter

from deps import ParametrizedClass
from fastapidi.utils.dependencies import ParameterizedDepends

router = APIRouter()


@router.get("/")
def root(parametrized_dep: ParametrizedClass = ParameterizedDepends(ParametrizedClass)):
    parametrized_dep.print_param()
    return {"message": "Hello World"}
