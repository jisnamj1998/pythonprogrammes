num=int(input("enter a number"))
is_fibonacci_no=False
previous=0
current=1
next=previous+current

while(next<=num):
    if next==num:
     is_fibonacci_no=True
     break
    previous=current
    current=next
    next=previous+current
print(is_fibonacci_no)    
#40-100 prime no
    

