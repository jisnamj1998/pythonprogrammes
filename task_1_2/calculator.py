num1=int(input("enter num1"))
num2=int(input("enter num2"))
operator=input("enter operator")

if operator=="+":
    result=num1+num2
    print(f"sum of {num1} and {num2} is {result}")
elif operator=="-":
    result=num1-num2
    print(f"difference of {num1} and {num2} is {result}")
elif operator=="*":
    result=num1*num2
    print(f"product of {num1} and {num2} is {result}")
elif operator=="/":
    result=num1/num2
    print(f"division of {num1} and {num2} is {result}") 
else:
    print("invalid operator")               