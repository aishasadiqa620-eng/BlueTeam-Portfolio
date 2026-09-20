# Task 1
with open("pakistan.txt","w") as file:
    file.write("user ali login success\n")
    file.write("user fatima login failed\n")
name=input("ap ka naam kia hy?")
print(f"user {name} login failed")
with open("pakistan.txt","r") as file:
    for line in file:
        if "failed" in line:
            print(f"mil gaya:{line.strip()}")
            