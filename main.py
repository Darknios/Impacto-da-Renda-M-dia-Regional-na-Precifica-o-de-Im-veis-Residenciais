from fastapi import FastAPI
from routes import auth_routes, dados_routes, analise_routes, previsao_routes

app = FastAPI(title="API - Impacto da Renda Média na Precificação de Imóveis")

# Rotas públicas (ex: login)
app.include_router(auth_routes.router)

# Rotas protegidas (dados, análises, predições)
app.include_router(dados_routes.router, prefix="/dados")
app.include_router(analise_routes.router, prefix="/analise")
app.include_router(previsao_routes.router, prefix="/previsao")
