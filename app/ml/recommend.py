from app.database import db
import random

def recommend_mechanic(service_name, user_location):
    service = db.service_types.find_one({"name": service_name})
    
    if not service:
        return {"error": "Service not found"}
    
    mechanic_ids = service["mechanics_available"]
    
    mechanics = list(db.mechanics.find({"_id": {"$in": mechanic_ids}}))
    
    recommended_mechanic = random.choice(mechanics) if mechanics else None
    
    return recommended_mechanic
