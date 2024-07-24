num=int(input("enter num"))
while(True):
    i=1
    n=0
    num+=1
    while(i<=num):
        if(num%i==0):
            n+=1
        i+=1
    if (n==2):
        print("next prime is",num)
        break        