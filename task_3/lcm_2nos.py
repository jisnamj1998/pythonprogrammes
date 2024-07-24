num1=int(input("enter num1"))
num2=int(input("enter num2"))
lcm=1
lar_no=num1 if num1>num2 else num2
while(True):
    if lar_no%num1==0 and lar_no%num2==0:
        lcm=lar_no
        break
    lar_no+=1
print(lcm)    