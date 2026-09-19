# Day 16 - soc log checker
with open("BlueTeam-Portfolio/fake_log.txt","r") as file:
    data = file.read()
    print("---Hamari log file---")
    print(data)
    if "Sargodha" in data:
        print("Alert: Sargodha wali analyst mil gye")
        print("Check Complete!")
        