ip="192.168.1.10"
failed=int(input("kitni baar login fail hua:"))
is_blocked=failed>=5
if is_blocked:
    print(f"Alert: IP {ip} KO BLOCK KRO! {failed} fails!")
else:
    print(f"IP {ip} Safe hai. Sirf {failed} fails.")
found = False
with open("company_log.txt","r") as file:
    for line in file:
        if "Failed" in line:
            found = True
            break  # Mil gaya, ab mazeed check karne ki zaroorat nahi
if found:
    print("Log file me Failed login mila!")
else:
    print("Log file clean ha")
with open("company_log.txt","r") as file:
    data=file.read()
    if "Failed" in data:
        print("haa")
    else:
        print("nhi")
        
