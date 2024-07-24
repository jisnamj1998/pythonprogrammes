num=input("enter num")
digit_count=len(num)
num=int(num)
original=num
sum=0
while(num!=0):
    digit=num%10
    exp=digit**digit_count
    sum=sum+exp
    num=num//10
    digit_count-=1
if original==sum:
    print("disarium number")
else:
    print("not disarium number")        
