from fastapi import APIRouter, HTTPException
from models.user_model import UserCreate
from config.database import db
from passlib.context import CryptContext

router = APIRouter()
pwd_context = CryptContext(schemes=["bcrypt"], deprecated="auto")

@router.post("/registrar")
async def registrar(user: UserCreate):
    existe = await db.usuarios.find_one({"username": user.username})
    if existe:
        raise HTTPException(status_code=400, detail="Usuário já existe")

    user_dict = user.dict()
    user_dict["password"] = pwd_context.hash(user.password)
    await db.usuarios.insert_one(user_dict)
    return {"msg": "Usuário cadastrado com sucesso"}

