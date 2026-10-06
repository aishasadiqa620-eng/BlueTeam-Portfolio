# Task 1
with open("BlueTeam-Portfolio/fake_log.txt","w") as f:
    f.write("user admin login failed\n")
    f.write("user ayesha login success\n")
print("ho gya")
with open("fake_log.txt","r") as file:
    data=file.read()
print(data)
with open("fake_log.txt","r") as f:
    for line in f:
        print(line)
with open("fake_log.txt","r") as file:
    for line in file:
        if "failed" in line:
            print(line)
my_name="Ayeaha"
print(f"Hello {my_name},Done day 16!")
user="admin"
result="failed"
with open("fake_log.txt","a") as f:
    f.write(f"user {user} login {result}\n")
my_name=input("Apna naam likho")
print(f"hello {my_name},Done day 16!")
user = input("Username likho: ")
print(f"user {user} login success")

with open("fake_log.txt", "w") as f:
    f.write(f"user {user} login success\n")
user=input("kis ka log dhoondna hy?")
with open("fake_log.txt","r") as f:
    for line in f:
        if user in line:
            print(f"mil gaya: {line.strip()}")
            



