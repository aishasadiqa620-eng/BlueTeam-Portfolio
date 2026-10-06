def show_failed():
    with open("fake_log.txt","r") as file:
        for line in file:
            if "failed" in line.lower():
                print(line)
show_failed()
def find_ip(ip):
    count=0
    with open("fake_log.txt","r") as file:
        for line in file:
            if ip in line:
                print(line.strip())
                count=count+1
    print(f"Total = {count}")
find_ip("203.45.67.89")
