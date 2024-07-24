num=input("enter a num")
digit_count=len(num)
num=int(num)
original=num
sum=0
while(num!=0):
    digit=num%10
    exp=digit**digit_count
    sum=sum+exp
    num=num//10
if original==sum:
    print("armstrong no")
else:
    print("not armstrong no") 
