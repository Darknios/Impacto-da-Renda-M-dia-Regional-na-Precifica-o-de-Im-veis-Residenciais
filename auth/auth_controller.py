from fastapi import HTTPException
from pydantic import BaseModel
from auth.jwt_handler import criar_token

class LoginInput(BaseModel):
    username: str
    password: str

def autenticar_usuario(data: LoginInput):
    if data.username == "ivson" and data.password == "123":
        token = criar_token({"sub": data.username})
        return {"token": token}
    raise HTTPException(status_code=401, detail="Usuário ou senha inválidos")
