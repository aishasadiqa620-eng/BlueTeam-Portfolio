def analyze_logs(ip_address):
    count=0
    found=False
    with open("fake_log.txt","r") as file:
        for line in file:
            if ip_address in line:
                print(line.strip())
                count+=1
                found=True
    
    print(f"Total attack = {count}")
    if found:
        print(f"ALERT: {ip_address} found!")
    else:
        print("Logs are clean")
        
