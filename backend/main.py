from backend.shared.attack_data import attacks
import random

attack = random.choice(list(attacks.keys()))

data = attacks[attack]

print("\n===== SentinelX Security Pipeline =====\n")

print(f"Attack Detected : {attack}")
print(f"MITRE Technique : {data['mitre']}")
print(f"Risk Score      : {data['risk']}/100")

print("\nGenerated Logs:")

for log in data["logs"]:
    print(f"  [LOG] {log}")

print("\nPipeline Status:")
print("  Attack Simulator  ✅")
print("  Log Generator     ✅")
print("  AI Defender       ✅")

print("\n=======================================\n")
