
from fastapi import APIRouter
router=APIRouter(tags=["Selection"])

@router.post("/selection")
def create_selection():
    return {"message":"selection created"}
