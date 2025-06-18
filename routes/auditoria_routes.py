from fastapi import APIRouter, Depends, Query
from auth.jwt_handler import verificar_token
from config.database import db
from datetime import datetime
from typing import Optional

router = APIRouter()

@router.get("/auditoria/logs", dependencies=[Depends(verificar_token)])
async def consultar_logs(
    usuario: Optional[str] = Query(None),
    rota: Optional[str] = Query(None),
    status: Optional[int] = Query(None),
    ip: Optional[str] = Query(None),
    data_inicio: Optional[str] = Query(None),
    data_fim: Optional[str] = Query(None)
):
    filtro = {}

    if usuario:
        filtro["usuario"] = {"$regex": usuario, "$options": "i"}
    if rota:
        filtro["rota"] = {"$regex": rota, "$options": "i"}
    if status:
        filtro["status"] = status
    if ip:
        filtro["ip"] = ip

    if data_inicio or data_fim:
        filtro["data"] = {}
        if data_inicio:
            filtro["data"]["$gte"] = datetime.fromisoformat(data_inicio)
        if data_fim:
            filtro["data"]["$lte"] = datetime.fromisoformat(data_fim)

    logs = await db.logs.find(filtro).sort("data", -1).to_list(100)
    for log in logs:
        log["_id"] = str(log["_id"])
    return logs
