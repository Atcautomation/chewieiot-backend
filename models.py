from sqlalchemy import Column, Integer, String, Float, DateTime
from datetime import datetime
from database import Base

class MeasuringPoint(Base):
    __tablename__ = "measuring_points"
    id = Column(Integer, primary_key=True, index=True)
    name = Column(String)
    mp_number = Column(String, unique=True)
    area = Column(String)
    subarea = Column(String)

class OEERecord(Base):
    __tablename__ = "oee_records"
    id = Column(Integer, primary_key=True, index=True)
    mp_id = Column(Integer)
    availability = Column(Float)
    performance = Column(Float)
    quality = Column(Float)
    oee = Column(Float)
    timestamp = Column(DateTime, default=datetime.utcnow)

