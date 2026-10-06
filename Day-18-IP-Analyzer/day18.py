count=0
found=False
with open("fake_log.txt","r") as file:
    for line in file:
        if "203.45.67.89" in line:
            print(line.strip())
            found=True
            count=count+1
print(f"Total attack = {count}")
if found:
    print("Alert: Hacker found in logs!")
else:
    print("Logs se clean")
    
