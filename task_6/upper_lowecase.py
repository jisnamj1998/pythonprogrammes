string=input("enter string")
lower_case=0
upper_case=0
for i in string:
    if (i.islower()):
        lower_case+=1
    elif (i.isupper()):
        upper_case+=1
print("lowercase count",lower_case)
print("uppercase count",upper_case) 