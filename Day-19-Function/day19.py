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
<<<<<<< HEAD
analyze_logs("203.45.67.89")        
=======
analyze_logs("203.45.67.89")
        
>>>>>>> 3651c76 (My practice)
