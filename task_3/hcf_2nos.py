num1=int(input("enter num1"))
num2=int(input("enter num2"))
hcf=1
i=1
least_no=num1 if num1<num2 else num2
while(i<=least_no):
    if num1%i==0 and num2%i==0:
        hcf=i
        
    i+=1
print(hcf)    