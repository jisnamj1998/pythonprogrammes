num1=int(input("enter num 1"))
num2=int(input("enter num 2"))
num3=int(input("enter num 3"))

if num1>num2 and num1>num3:
    print("largest num is num1")
    if num2>num3:
        print("sec lar is num2")
         
    elif num3>num2:
        print("sec lar is num3")

elif num2>num1 and num2>num3:
    print("largest num is num2")
    if num1>num3:
        print("sec large is num1")
    elif num3>num1:
        print("sec large is num3")    
elif num3>num1 and num3>num2:
    print("largest num is num3")
    if num1>num2:
        print("sec large is num1")
    elif num2>num1:
        print("sec large is num2")
