from backend.report_generator.report_generator import generate_report
from backend.shared.timeline import generate_timeline
from backend.shared.soc_alert import generate_alert
from backend.shared.severity_engine import calculate_severity
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
severity = calculate_severity(
    data["risk"],
    target["criticality"]
)
alert = generate_alert(
    incident_id,
    attack,
    severity,
    target
)


print("\n===== SentinelX Security Pipeline =====\n")

print(f"Incident ID     : {incident_id}")

print(f"\nAttack Detected : {attack}")
print(f"Target Asset    : {target['id']}")
print(f"Asset Type      : {target['type']}")
print(f"Criticality     : {target['criticality']}")

print(f"\nMITRE Technique : {data['mitre']}")
print(f"Risk Score      : {data['risk']}/100")
print(f"Severity        : {severity}")
print("\nGenerated Logs:")

for log in data["logs"]:
    print(f"  [LOG] {log}")

print(alert)

timeline = generate_timeline()

report = generate_report(
    incident_id,
    attack,
    target,
    severity,
    data["mitre"],
    data["logs"],
    timeline
)

print("\nIncident Timeline:")

for event in timeline:
    print(f"  {event}")
    
print("\nPipeline Status:")
print("  Attack Simulator  ✅")
print("  Log Generator     ✅")
print("  AI Defender       ✅")

print("\n=======================================\n")

print(report)
