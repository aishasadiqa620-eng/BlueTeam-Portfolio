# 1. Variables
ip_address = "192.168.1.10"
failed_attempts = 4

# 2. Task 1: int check
# Agar failed_attempts 5 se zyada hai to "Block IP" warna "Allow IP"
if failed_attempts > 5:
    print("Block IP: " + ip_address)
else:
    print("Allow IP: " + ip_address)

# 3. Task 2: bool check (Ye tum likhoge)
is_admin = False
if is_admin:
    print("Welcome Admin")
else:
    print("Welcome user")
# 4. Task 3: str check (Ye bhi tum likhoge)
status = "failed"
if status=="failed":
    print("login failed")
else:
    print("login success")

