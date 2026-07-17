
from fastapi import APIRouter
router=APIRouter(tags=["Retrieval"])

@router.get("/testcases/{selection_id}")
def get_cases(selection_id:int):
    return {"selection_id":selection_id}
