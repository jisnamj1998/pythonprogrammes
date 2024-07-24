previous=0
current=1
print(previous)
print(current)
limit=100
next=1
while(next<=limit):
    print(next)
    previous=current
    current=next
    next=previous+current
    #if we write next=prev+curr in 8th line o/p will end greater than 100