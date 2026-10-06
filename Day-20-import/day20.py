import datetime
abhi = datetime.datetime.now()
ghanta = abhi.hour
if ghanta >=22 or ghanta <=6:
    print("Alert! Raat ko kaam ho rha hai,ye hack ho skta ha!")
else:
    print("Normal din ka kaam hai")
