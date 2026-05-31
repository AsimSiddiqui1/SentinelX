import random

attacks = [
    "Brute Force",
    "Phishing",
    "Ransomware",
    "Web Exploitation"
]

attack = random.choice(attacks)

print(f"Simulating Attack: {attack}")
