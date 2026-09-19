# Task 1
with open("soc_log.txt","w") as file:
    file.write("user Ali login success\n")
    file.write("user Sara login failed\n")
    file.write("user Ahmed login failed\n")
user=input("Apka naam kia hy?")
with open("soc_log.txt","a") as file:
    file.write(f"user {user} login failed\n")
with open("soc_log.txt","r") as file:
    for line in file:
        if "failed" in line:
            print(line)
            