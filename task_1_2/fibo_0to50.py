previous=0
current=1
print(previous)
print(current)
limit=50
next=1
while(next<=limit):
    print(next)
    previous=current
    current=next
    next=previous+current