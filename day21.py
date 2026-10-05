import re
with open("log2.txt","r") as file:
    for line in file:
        ip =re.findall(r"\d+\.\d+\.\d+\.\d+",line)
        email =re.findall(r"alert\s+([\w\.-]+@[\w\.-]+\.\w+)",line)
        username =re.findall(r"alert\s+([\w\.-]+)@",line)
        domain =re.findall(r"@([\w\.-]+\.\w+)",line)
        print(ip)
        print(email)
        print(username)
        print(domain)
