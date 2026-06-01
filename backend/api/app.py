from backend.attack_engine.attack_simulator import simulate_attack
from backend.ai_defender.ai_defender import detect_attack
from backend.database.incident_history import incident_history
from fastapi.responses import FileResponse
from fastapi.middleware.cors import CORSMiddleware
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

app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

@app.get("/")
def home():
    return {
        "message": "Welcome to SentinelX"
    }

@app.get("/dashboard")
def dashboard():
    return FileResponse("backend/templates/index.html")
    
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
@app.get("/launch/{attack_type}")
def launch_attack(attack_type: str):

    print("Selected:", attack_type)

    result = simulate_attack(attack_type)

    print("Result:", result)

    detected_attack = detect_attack(
        result["logs"]
    )

print("Detected:", detected_attack)

if detected_attack == "Unknown":
    return {
        "error": "Unknown attack",
        "logs": result["logs"]
    }

data = attacks[detected_attack]

target = random.choice(assets)

incident_id = generate_incident_id()

severity = calculate_severity(
    data["risk"],
    target["criticality"]
)

timeline = generate_timeline()

incident_history.append({
    "incident_id": incident_id,
    "attack": detected_attack,
    "severity": severity,
    "asset": target["id"]
})

return {
    "incident_id": incident_id,
    "attack": detected_attack,
    "mitre": data["mitre"],
    "severity": severity,
    "risk_score": data["risk"],
    "target_asset": target["id"],
    "logs": result["logs"],
    "timeline": timeline
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

    incident_history.append({
        "incident_id": incident_id,
        "attack": attack,
        "severity": severity,
        "asset": target["id"]
    })

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

@app.get("/history")
def history():
    return incident_history
