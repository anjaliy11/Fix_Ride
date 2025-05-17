import os
import pymongo
from dotenv import load_dotenv

load_dotenv()

MONGO_URI = os.getenv("MONGO_URI")  # Load from .env file

client = pymongo.MongoClient(MONGO_URI)
db = client["Mechanic_Services"]
