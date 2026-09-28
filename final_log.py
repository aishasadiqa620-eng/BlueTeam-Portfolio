search_word=input("Kia search karna hai?")
count=0
found=False
with open("company_log.txt","r") as file:
    for line in file:
        if search_word.lower() in line.lower():
            count=count+1
            found=True
print(f"Count ka type: {type(count)}")
print(f"found ka type: {type(found)}")
if found:
    print(f"Alert! total {count} baar attack mila")
else:
    print("System Safe - Kuch nhi mila")
    