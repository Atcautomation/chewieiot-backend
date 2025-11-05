from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from models import MeasuringPoint

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def list_mps(db: Session = Depends(get_db)):
    """List all Measuring Points"""
    return db.query(MeasuringPoint).all()

@router.post("/seed")
def seed_test_mps(db: Session = Depends(get_db)):
    """Insert sample measuring points if table is empty"""
    if db.query(MeasuringPoint).count() == 0:
        samples = [
            MeasuringPoint(name="Sorter Control", mp_number="303111702", area="Sorter", subarea="Control"),
            MeasuringPoint(name="Chute 1", mp_number="303112403", area="Sorter", subarea="Chutes"),
            MeasuringPoint(name="Conveyor 2", mp_number="303140200", area="Sorter", subarea="Conveyor"),
        ]
        db.add_all(samples)
        db.commit()
        return {"message": "Sample measuring points added"}
    else:
        return {"message": "Data already exists"}
