from fastapi import FastAPI
from routes import auth_routes, dados_routes, analise_routes, previsao_routes, user_routes
from middleware.log_to_mongo import log_para_mongo

app = FastAPI(title="API - Impacto da Renda Média na Precificação de Imóveis")

# Middleware de log
app.middleware("http")(log_para_mongo)


# Rotas públicas 
app.include_router(auth_routes.router)
app.include_router(user_routes.router)

# Rotas protegidas
app.include_router(dados_routes.router, prefix="/dados")
app.include_router(analise_routes.router, prefix="/analise")
app.include_router(previsao_routes.router, prefix="/previsao")


