import datetime
with open("log.txt","r") as file:
    for line in file:
        time_wala_hissa =line.split(",")[0]
        log_time = datetime.datetime.strptime(time_wala_hissa,"%Y-%m-%d %H:%M:%S")
        ghanta = log_time.hour
        if ghanta >=22 or ghanta <=6:
            print(f"Alert! {log_time} par raat ko login hua!")
        else:
            print(f"Normal! {log_time} par din ko login hua!")