from fastapi import FastAPI
import random

from backend.shared.attack_data import attacks
from backend.database.assets import assets

app = FastAPI(
    title="SentinelX API",
    version="1.0"
)

@app.get("/")
def home():
    return {
        "message": "Welcome to SentinelX"
    }

@app.get("/simulate")
def simulate():

    attack = random.choice(list(attacks.keys()))
    data = attacks[attack]

    target = random.choice(assets)

    return {
        "attack": attack,
        "mitre": data["mitre"],
        "risk_score": data["risk"],
        "target_asset": target["id"],
        "asset_type": target["type"],
        "criticality": target["criticality"]
    }
