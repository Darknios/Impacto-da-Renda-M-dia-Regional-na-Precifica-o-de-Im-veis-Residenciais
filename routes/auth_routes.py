from fastapi import APIRouter
from auth.auth_controller import LoginInput, autenticar_usuario

router = APIRouter()

@router.post("/login")
async def login(data: LoginInput):
    return await autenticar_usuario(data)  