# Day 17 - Brute Force Detector - Aisha

# 1. Sample logs - ek hi IP se kitni baar fail login hua
failed_logins = {
    "192.168.1.10": 3,
    "10.0.0.5": 9,
    "192.168.1.15": 6
}

# 2. Threshold - 5 se zyada fail = Brute Force
threshold = 5

print("--- Brute Force Check Start ---")

for ip, fails in failed_logins.items():
    print(f"\nIP {ip} ne {fails} baar fail kiya")
    
    if fails > threshold:
        print(f"ALERT! {ip} ko Block karo! Brute Force attack hai")
    else:
        print(f"Safe hai, {ip} par kuch nahi karna")



