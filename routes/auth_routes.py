from fastapi import APIRouter
from auth.auth_controller import LoginInput, autenticar_usuario

router = APIRouter()

@router.post("/login")
def login(data: LoginInput):
    return autenticar_usuario(data)
