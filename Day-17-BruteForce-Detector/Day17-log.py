found=False
with open("company_log.txt","r") as file:
    for line in file:
        if "Failed" in line:
            found=True
            break
if found:
    print("Attack Mila")
else:
    print("Sab Safe Hai!")
# Din 17 - Task: Log Checker
print("--- SOC Log Checker ---")

# Step 1: File kholo (Din 16 wala kaam)
file = open("company_log.txt", "r")
data = file.read()

# Step 2: User se pucho konsa word check karna hai
word = input("Konsa word check karna hai? (Failed / Success): ")

# Step 3: if/else (Din 17 wala kaam)
if word in data:
    print(f"ALERT! '{word}' log me mila - Check karna parega")
    # Extra data type check
    print("Data type:", type(data))
else:
    print(f"'{word}' nahi mila - System Safe")

file.close()    
