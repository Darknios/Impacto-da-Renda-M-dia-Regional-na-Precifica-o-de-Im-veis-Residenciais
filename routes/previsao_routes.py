from fastapi import APIRouter, Depends
from pydantic import BaseModel
from auth.jwt_handler import verificar_token
import pandas as pd
import joblib

from sklearn.ensemble import RandomForestRegressor

router = APIRouter()
df = pd.read_csv("data/dados.csv")

features = ['Area', 'Quartos', 'Banheiros', 'NumAndares', 'VagasGaragem']
df = df.dropna(subset=features + ['Preco'])
model = RandomForestRegressor().fit(df[features], df['Preco'])

class ImovelInput(BaseModel):
    Area: float
    Quartos: int
    Banheiros: int
    NumAndares: int
    VagasGaragem: int

class PrevisaoInput(ImovelInput):
    PrecoReal: float

@router.post("/valor", dependencies=[Depends(verificar_token)])
def prever_valor(imovel: ImovelInput):
    dados = [[
        imovel.Area,
        imovel.Quartos,
        imovel.Banheiros,
        imovel.NumAndares,
        imovel.VagasGaragem
    ]]
    valor = model.predict(dados)[0]
    return {"preco_previsto": round(valor, 2)}

@router.post("/classificar", dependencies=[Depends(verificar_token)])
def classificar_preco(dados: PrevisaoInput):
    previsao = prever_valor(dados)
    previsto = previsao["preco_previsto"]
    erro = ((dados.PrecoReal - previsto) / previsto) * 100

    if abs(erro) <= 10:
        classificacao = "Justo"
    elif erro > 10:
        classificacao = "Caro"
    else:
        classificacao = "Barato"

    return {
        "preco_previsto": previsto,
        "preco_real": dados.PrecoReal,
        "erro_percentual": round(erro, 2),
        "classificacao": classificacao
    }
