import pandas as pd
import numpy as np

# Generate fake vehicle data
vehicles = pd.DataFrame({
    "Vehicle_ID": [f"V{i}" for i in range(1, 21)],
    "Type": np.random.choice(["Truck", "Van", "EV"], size=20),
    "Max_Load_kg": np.random.randint(1000, 5000, size=20),
    "Fuel_Efficiency_kmpl": np.random.uniform(5, 15, size=20),  # km per liter
    "CO2_Emission_gkm": np.random.uniform(150, 300, size=20)  # grams per km
})

# Generate fake route data
routes = pd.DataFrame({
    "Route_ID": [f"R{i}" for i in range(1, 31)],
    "Distance_km": np.random.randint(50, 500, size=30),
    "Traffic_Condition": np.random.choice(["Low", "Medium", "High"], size=30),
    "Topography": np.random.choice(["Flat", "Hilly", "Urban"], size=30)
})

# Generate fake shipment data
shipments = pd.DataFrame({
    "Shipment_ID": [f"S{i}" for i in range(1, 51)],
    "Route_ID": np.random.choice(routes["Route_ID"], size=50),
    "Vehicle_ID": np.random.choice(vehicles["Vehicle_ID"], size=50),
    "Load_kg": np.random.randint(500, 4000, size=50)
})

print("Vehicles:\n", vehicles.head())
print("Routes:\n", routes.head())
print("Shipments:\n", shipments.head())
