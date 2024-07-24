num=str(153)
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
    print("armstrong number")
else:
    print("not armstrong number")        
