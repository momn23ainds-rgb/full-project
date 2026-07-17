
from fastapi import APIRouter
router=APIRouter(tags=["Generation"])

@router.post("/generate/{selection_id}")
def generate(selection_id:int):
    return {"selection_id":selection_id}
