from fastapi import APIRouter, Depends
from app.api.dependencies import require_admin, require_role
from app.models.user import User


router = APIRouter(
    prefix="/admin",
    tags=["Admin"],
    dependencies=[Depends(require_role(["admin"]))]
)


@router.get("/dashboard")
def admin_dashboard(
    admin: User = Depends(require_admin),
):
    return {
        "message": f"Bem-vindo admin {admin .email}"
    }


@router.get("/dashboard")
def dashboard():
    return {"msg": "Acessdo admin autorizado"}

