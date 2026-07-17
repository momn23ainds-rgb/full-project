
from fastapi import APIRouter
router=APIRouter(tags=["Browse"])

@router.get("/sections")
def sections():
    return []
