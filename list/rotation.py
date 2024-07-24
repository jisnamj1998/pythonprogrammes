list=[1,2,3,4,5,6,7]
# rotate 2 times
#o/p list=[6,7,1,2,3,4,5]
k=2
for i in range(0,k):
    last_element=list.pop()
    list.insert(0,last_element)
print(list)    
    
