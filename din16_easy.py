# mera pehla easy task
analyst = input("Ap ka naam?")
city = input("City ka naam?")
print(f"Hello analyst {analyst} from {city}")
with open("BlueTeam-Portfolio/fake_log.txt","a") as file:
    file.write(f"Analyst {analyst} from {city} logged in\n")
    print("Ho gya!")
    


