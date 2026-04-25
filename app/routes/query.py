from fastapi import APIRouter
from app.orchestrator import handle_query

router = APIRouter()

@router.post("/query")
def query_endpoint(payload: dict):
    user_query = payload.get("query")
    return handle_query(user_query)