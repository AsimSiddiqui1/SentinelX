import random
from datetime import datetime

attacks = {
    "Brute Force": "T1110",
    "Phishing": "T1566",
    "Ransomware": "T1486",
    "Web Exploitation": "T1190"
}

attack = random.choice(list(attacks.keys()))

print("\n===== SentinelX Attack Simulator =====")
print(f"Time: {datetime.now()}")
print(f"Attack Type: {attack}")
print(f"MITRE ATT&CK: {attacks[attack]}")
print("Status: Attack Executed")
print("=====================================\n")
