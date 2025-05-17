import random
import json
import pandas as pd
from faker import Faker
from datetime import datetime, timedelta

# Initialize Faker for realistic names and locations
fake = Faker()

# Constants
NUM_USERS = 3000
NUM_MECHANICS = 500
NUM_TRANSACTIONS = 5000

# Vehicle types
VEHICLE_TYPES = ["Car", "Bike", "Truck", "Electric Vehicle"]

# Service types
SERVICE_TYPES = [
    "Engine Repair", "Battery Change", "Oil Change", "Brake Repair", "Tire Replacement",
    "Transmission Repair", "AC Service", "Suspension Fix", "Wheel Alignment", "General Service"
]

# Generate Mechanics Data
mechanics = []
for i in range(NUM_MECHANICS):
    mechanics.append({
        "mechanic_id": f"mech_{i}",
        "name": fake.name(),
        "service_types": random.sample(SERVICE_TYPES, random.randint(1, 5)),
        "experience_years": random.randint(1, 20),
        "ratings": round(random.uniform(3.0, 5.0), 1),
        "response_time": round(random.uniform(5, 60), 1),  # in minutes
        "availability": random.choice(["Available", "Busy"]),
        "location": {"lat": round(random.uniform(20.0, 30.0), 6), "long": round(random.uniform(70.0, 80.0), 6)}
    })

# Generate Users Data
users = []
for i in range(NUM_USERS):
    users.append({
        "user_id": f"user_{i}",
        "name": fake.name(),
        "gender": random.choice(["Male", "Female", "Other"]),
        "location": {"lat": round(random.uniform(20.0, 30.0), 6), "long": round(random.uniform(70.0, 80.0), 6)},
        "vehicle_type": random.choice(VEHICLE_TYPES),
        "preferred_mechanics": random.sample([m["mechanic_id"] for m in mechanics], random.randint(1, 5)),
        "past_service_history": [
            {"mechanic_id": random.choice(mechanics)["mechanic_id"], "service_type": random.choice(SERVICE_TYPES),
             "rating": round(random.uniform(3.0, 5.0), 1)}
            for _ in range(random.randint(1, 10))
        ]
    })

# Generate Service Requests / Transactions Data
transactions = []
for i in range(NUM_TRANSACTIONS):
    user = random.choice(users)
    mechanic = random.choice(mechanics)
    service_type = random.choice(SERVICE_TYPES)
    start_time = datetime.now() - timedelta(days=random.randint(0, 365))
    completion_time = start_time + timedelta(minutes=random.randint(30, 180))

    transactions.append({
        "transaction_id": f"txn_{i}",
        "user_id": user["user_id"],
        "mechanic_id": mechanic["mechanic_id"],
        "service_type": service_type,
        "time_of_request": start_time.strftime("%Y-%m-%d %H:%M:%S"),
        "time_taken": (completion_time - start_time).seconds // 60,  # in minutes
        "cost": round(random.uniform(500, 5000), 2),
        "user_feedback": round(random.uniform(3.0, 5.0), 1)
    })

# Save to JSON
with open("users.json", "w") as f:
    json.dump(users, f, indent=4)

with open("mechanics.json", "w") as f:
    json.dump(mechanics, f, indent=4)

with open("transactions.json", "w") as f:
    json.dump(transactions, f, indent=4)

# Convert to DataFrames and Save as CSV
pd.DataFrame(users).to_csv("users.csv", index=False)
pd.DataFrame(mechanics).to_csv("mechanics.csv", index=False)
pd.DataFrame(transactions).to_csv("transactions.csv", index=False)

print(" Data successfully generated ")
