limit=int(input("enter limit"))
sum=0
for i in range(0,limit+1):
    if i%2!=0:
        sum=sum+i
    i+=1   
print(sum)     