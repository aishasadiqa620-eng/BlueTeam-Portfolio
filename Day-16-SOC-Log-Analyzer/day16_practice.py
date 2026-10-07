# Task 1 - Day 16 - SOC Log Analyzer ki shuruat

# Step 1: Fake log banao
with open("fake_log.txt","w") as f:
    f.write("user admin login failed\n")
    f.write("user ayesha login success\n")
    f.write("user admin login failed\n")

print("Log file ban gayi!")

# Step 2: Saari logs padho
print("\n--- Saari Logs ---")
with open("fake_log.txt","r") as file:
    for line in file:
        print(line.strip())

# Step 3: Sirf failed wali dhoondo (Yehi SOC Analyst ka kaam hai)
print("\n--- Sirf Failed Logins ---")
with open("fake_log.txt","r") as file:
    for line in file:
        if "failed" in line:
            print(f"ALERT: {line.strip()}")

# Step 4: User se pucho
user = input("\nKis ka log dhoondna hai? ")
with open("fake_log.txt","r") as f:
    for line in f:
        if user in line:
            print(f"Mil gaya: {line.strip()}")
            



