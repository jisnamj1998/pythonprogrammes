num=151
result=""
original=num
while(num!=0):
    digit=num%10
    result=result+str(digit)
    num=num//10
print(result)
if original==int(result):
    print("palindrome")
else:
    print("not palindrome")      