from fastapi import FastAPI
from app.routes import mechanics, services, users

app = FastAPI(title="Mechanic Services API")

# Include API routes
app.include_router(users.router, prefix="/api/users", tags=["Users"])
app.include_router(mechanics.router, prefix="/api/mechanics", tags=["Mechanics"])
app.include_router(services.router, prefix="/api/services", tags=["Services"])

@app.get("/")
async def root():
    return {"message": "Welcome to Mechanic Services API"}
