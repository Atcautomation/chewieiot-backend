from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from database import SessionLocal
from models import OEERecord
from datetime import datetime, timedelta
import random

router = APIRouter()

def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()

@router.get("/")
def list_oee(db: Session = Depends(get_db)):
    """List all OEE records"""
    return db.query(OEERecord).all()

@router.post("/seed")
def seed_test_oee(db: Session = Depends(get_db)):
    """Generate sample OEE data"""
    if db.query(OEERecord).count() == 0:
        now = datetime.utcnow()
        samples = []
        for i in range(1, 4):  # simulate 3 MPs
            for h in range(8):  # 8 data points each
                a = round(random.uniform(80, 100), 2)
                p = round(random.uniform(70, 95), 2)
                q = round(random.uniform(85, 100), 2)
                samples.append(OEERecord(
                    mp_id=i,
                    availability=a,
                    performance=p,
                    quality=q,
                    oee=round((a*p*q)/10000, 2),
                    timestamp=now - timedelta(hours=h)
                ))
        db.add_all(samples)
        db.commit()
        return {"message": "Sample OEE data added"}
    else:
        return {"message": "OEE data already exists"}
