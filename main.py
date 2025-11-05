from fastapi import FastAPI
from routers import oee, mp
from database import init_db

app = FastAPI(title="ChewieIoT Cloud API")

@app.on_event("startup")
def startup_event():
    init_db()

app.include_router(oee.router, prefix="/api/oee", tags=["OEE"])
app.include_router(mp.router, prefix="/api/mp", tags=["Measuring Points"])

@app.get("/")
def root():
    return {"message": "Welcome to ChewieIoT Cloud"}
