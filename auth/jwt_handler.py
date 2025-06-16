from jose import JWTError, jwt
from datetime import datetime, timedelta
from fastapi import HTTPException, status, Depends
from fastapi.security import HTTPBearer, HTTPAuthorizationCredentials
import os
from dotenv import load_dotenv

load_dotenv()  

SEGREDO = os.getenv("SEGREDO_JWT")
ALGORITMO = os.getenv("ALGORITMO_JWT", "HS256")
EXPIRA_EM_MINUTOS = int(os.getenv("EXPIRA_MINUTOS", 30))

auth_scheme = HTTPBearer()

def criar_token(data: dict):
    expira = datetime.utcnow() + timedelta(minutes=EXPIRA_EM_MINUTOS)
    payload = {**data, "exp": expira}
    token = jwt.encode(payload, SEGREDO, algorithm=ALGORITMO)
    return token

def verificar_token(token: HTTPAuthorizationCredentials = Depends(auth_scheme)):
    try:
        payload = jwt.decode(token.credentials, SEGREDO, algorithms=[ALGORITMO])
        return payload
    except JWTError:
        raise HTTPException(status_code=status.HTTP_401_UNAUTHORIZED, detail="Token inválido")
