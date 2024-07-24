num=int(input("enter a num"))
is_prime=True
if num==1:
    print(is_prime=False)
# elif num==2:
#     print(is_prime=True)    

else:
    for i in range(2,num):
     if(num%i==0):
        is_prime=False
        break
print(is_prime)    