from fastapi import APIRouter, Depends
from db.database import get_db
from sqlalchemy.orm import Session
from sqlalchemy import text

router = APIRouter(
    tags=["Health"]
)

@router.get('/health')
def health_check():
    return {"status": "UP"}

@router.get("/ready")
def ready_check(db:Session=Depends(get_db)):
   try:
       db.execute(text("SELECT 1"))

       return {
           "status": "READY",
           "database": "UP"
       }
   except Exception as e:
       return {
           "status": "NOT_READY",
           "database": "DOWN",
           "error": str(e)
       }
