import pandas as pd
from sklearn.preprocessing import MinMaxScaler

# Load datasets
df_users = pd.read_json("data/users.json")
df_mechanics = pd.read_json("data/mechanics.json")
df_service_requests = pd.read_json("data/transactions.json")

# Extract lat and long from nested 'location' dictionary
df_users["lat"] = df_users["location"].apply(lambda x: x["lat"] if isinstance(x, dict) and "lat" in x else None)
df_users["long"] = df_users["location"].apply(lambda x: x["long"] if isinstance(x, dict) and "long" in x else None)
df_users.drop(columns=["location"], inplace=True)

# Extract lat and long for mechanics
df_mechanics["lat"] = df_mechanics["location"].apply(lambda x: x["lat"] if isinstance(x, dict) and "lat" in x else None)
df_mechanics["long"] = df_mechanics["location"].apply(lambda x: x["long"] if isinstance(x, dict) and "long" in x else None)
df_mechanics.drop(columns=["location"], inplace=True)

# Fill missing values
df_service_requests.fillna({"cost": df_service_requests["cost"].median()}, inplace=True)
df_users.fillna("Unknown", inplace=True)
df_mechanics.fillna("Unknown", inplace=True)

# Normalize lat-long values
scaler = MinMaxScaler()
df_users[["lat", "long"]] = scaler.fit_transform(df_users[["lat", "long"]])
df_mechanics[["lat", "long"]] = scaler.fit_transform(df_mechanics[["lat", "long"]])

# Save preprocessed data
df_users.to_csv("data/preprocessed_users.csv", index=False)
df_mechanics.to_csv("data/preprocessed_mechanics.csv", index=False)
df_service_requests.to_csv("data/preprocessed_service_requests.csv", index=False)

print("Preprocessing complete! Data saved to CSV files.")
