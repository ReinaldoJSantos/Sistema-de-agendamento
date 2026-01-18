from fastapi import APIRouter, Depends
from app.api.dependencies import require_role


router = APIRouter(
    prefix="/admin",
    tags=["Admin"],
    dependencies=[Depends(require_role(["admin"]))]
)


@router.get("/dashboard")
def dashboard():
    return {"msg": "Acessdo admin autorizado"}