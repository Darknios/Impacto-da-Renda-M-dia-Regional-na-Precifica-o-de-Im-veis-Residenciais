from fastapi import HTTPException
from models.user_model import LoginInput
from auth.jwt_handler import criar_token
from config.database import db
from passlib.context import CryptContext

pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

async def autenticar_usuario(data: LoginInput):
    usuario = await db.usuarios.find_one({"username": data.username})

    if not usuario:
        raise HTTPException(status_code=404, detail="Usuário não encontrado")

    try:
        senha_ok = pwd_context.verify(data.password, usuario["password"])
    except Exception:
        raise HTTPException(status_code=500, detail="Erro ao verificar a senha")

    if not senha_ok:
        raise HTTPException(status_code=401, detail="Senha incorreta")

    token = criar_token({"sub": usuario["username"]})
    return {
        "token": token,
        "username": usuario["username"]
    }
