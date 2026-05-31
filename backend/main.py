from backend.shared.attack_data import attacks
from backend.database.assets import assets
import random

# Select attack
attack = random.choice(list(attacks.keys()))
data = attacks[attack]

# Select target asset
target = random.choice(assets)

print("\n===== SentinelX Security Pipeline =====\n")

print(f"Attack Detected : {attack}")
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
