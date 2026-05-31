from backend.shared.incident_manager import generate_incident_id
from backend.shared.severity_engine import calculate_severity
from backend.shared.timeline import generate_timeline
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

@app.get("/incident")
def incident():

    attack = random.choice(list(attacks.keys()))
    data = attacks[attack]

    target = random.choice(assets)

    incident_id = generate_incident_id()

    severity = calculate_severity(
        data["risk"],
        target["criticality"]
    )

    timeline = generate_timeline()

    return {
        "incident_id": incident_id,
        "attack": attack,
        "mitre": data["mitre"],
        "severity": severity,
        "risk_score": data["risk"],
        "target_asset": target["id"],
        "logs": data["logs"],
        "timeline": timeline
    }
