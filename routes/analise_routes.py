from fastapi import APIRouter, Depends
from auth.jwt_handler import verificar_token
import pandas as pd

router = APIRouter()
df = pd.read_csv("data/dados.csv")

@router.get("/media-estado", dependencies=[Depends(verificar_token)])
def media_por_estado():
    return df.groupby("estado")["preco"].mean().to_dict()

@router.get("/media-regiao", dependencies=[Depends(verificar_token)])
def media_por_regiao():
    return df.groupby("regiao")["preco"].mean().to_dict()

@router.get("/proporcao-acima-media", dependencies=[Depends(verificar_token)])
def proporcao_estado_acima_media():
    proporcao = df.groupby("estado")["acima_media_regiao"].mean()
    return proporcao.round(3).to_dict()

@router.get("/top-fatores", dependencies=[Depends(verificar_token)])
def top_fatores():
    fatores = {
        "PE": ["Banheiros", "Area", "NumAndares"],
        "PI": ["Banheiros", "NumAndares", "Area"],
        "RN": ["NumAndares", "Banheiros", "Area"]
    }
    return fatores
