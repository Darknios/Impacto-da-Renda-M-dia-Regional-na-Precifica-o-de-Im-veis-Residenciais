import logging
from datetime import datetime
from fastapi import Request
from config.database import db


logging.basicConfig(
    filename="logs/app.log",
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

async def log_para_mongo(request: Request, call_next):
    ip = request.client.host
    rota = request.url.path
    metodo = request.method
    usuario = request.headers.get("authorization", "anônimo")

    data_hora = datetime.utcnow()
    response = await call_next(request)
    status = response.status_code

    
    logging.info(f"{metodo} {rota} | IP: {ip} | Usuário: {usuario} | Status: {status}")

    
    log_document = {
        "ip": ip,
        "rota": rota,
        "metodo": metodo,
        "usuario": usuario,
        "status": status,
        "data": data_hora
    }
    await db.logs.insert_one(log_document)

    return response
