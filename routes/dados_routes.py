from fastapi import APIRouter, Depends, Query
from auth.jwt_handler import verificar_token
import pandas as pd

router = APIRouter()
df = pd.read_csv("data/dados.csv")

@router.get("/imoveis", dependencies=[Depends(verificar_token)])
def listar_imoveis(skip: int = 0, limit: int = 50):
    return df.iloc[skip:skip+limit].to_dict(orient="records")

@router.get("/filtrar", dependencies=[Depends(verificar_token)])
def filtrar(
    estado: str = Query(None),
    cidade: str = Query(None),
    tipo_imovel: str = Query(None),
    preco_min: float = Query(None),
    preco_max: float = Query(None),
    area_min: float = Query(None),
    area_max: float = Query(None)
):
    resultado = df.copy()

    if estado:
        resultado = resultado[resultado["estado"].str.upper() == estado.upper()]
    if cidade:
        resultado = resultado[resultado["cidade"].str.upper() == cidade.upper()]
    if tipo_imovel:
        resultado = resultado[resultado["tipo_imovel"].str.upper() == tipo_imovel.upper()]
    if preco_min:
        resultado = resultado[resultado["preco"] >= preco_min]
    if preco_max:
        resultado = resultado[resultado["preco"] <= preco_max]
    if area_min:
        resultado = resultado[resultado["area_m2"] >= area_min]
    if area_max:
        resultado = resultado[resultado["area_m2"] <= area_max]

    return resultado.to_dict(orient="records")
