for num in range(1,100):
    digit_count=len(str(num))
    sum=0
    original=num
    while(original>0):
        digit=original%10
        exp=digit**digit_count
        sum=sum+exp
        original=original//10
    if num==sum:
        print(num)    
