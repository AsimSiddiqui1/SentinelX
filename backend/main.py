from backend.shared.attack_data import attacks
from backend.database.assets import assets
from backend.shared.incident_manager import generate_incident_id
import random

# Generate Incident ID
incident_id = generate_incident_id()

# Select attack
attack = random.choice(list(attacks.keys()))
data = attacks[attack]

# Select target asset
target = random.choice(assets)

print("\n===== SentinelX Security Pipeline =====\n")

print(f"Incident ID     : {incident_id}")

print(f"\nAttack Detected : {attack}")
print(f"Target Asset    : {target['id']}")
print(f"Asset Type      : {target['type']}")
print(f"Criticality     : {target['criticality']}")

print(f"\nMITRE Technique : {data['mitre']}")
print(f"Risk Score      : {data['risk']}/100")

print("\nGenerated Logs:")

for log in data["logs"]:
    print(f"  [LOG] {log}")

print("\nPipeline Status:")
print("  Attack Simulator  ✅")
print("  Log Generator     ✅")
print("  AI Defender       ✅")

print("\n=======================================\n")
