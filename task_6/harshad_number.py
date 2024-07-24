num=input("enter number")
num=int(num)
original=num
sum=0
while(num!=0):
    digit=num%10
    sum=sum+digit
    num=num//10
if (original%sum==0):
    print("harshad number")
else:
    print("not harshad number")        
