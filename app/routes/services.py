from fastapi import APIRouter
from app.database import db
from app.models.service_type import ServiceType

router = APIRouter()

@router.get("/")
async def get_services():
    services = list(db.service_types.find({}, {"_id": 0}))
    return {"services": services}

@router.post("/")
async def add_service(service: ServiceType):
    db.service_types.insert_one(service.dict())
    return {"message": "Service added successfully"}
