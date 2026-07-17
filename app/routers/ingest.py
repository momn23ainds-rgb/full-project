
from fastapi import APIRouter
router=APIRouter(tags=["Ingest"])

@router.post("/ingest")
def ingest():
    return {"message":"Implement ingestion here"}
