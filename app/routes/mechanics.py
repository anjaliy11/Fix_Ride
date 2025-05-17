from fastapi import APIRouter
from app.database import db
from app.models.mechanic import Mechanic

router = APIRouter()

@router.get("/")
async def get_mechanics():
    mechanics = list(db.mechanics.find({}, {"_id": 0}))
    return {"mechanics": mechanics}

@router.post("/")
async def add_mechanic(mechanic: Mechanic):
    db.mechanics.insert_one(mechanic.dict())
    return {"message": "Mechanic added successfully"}
