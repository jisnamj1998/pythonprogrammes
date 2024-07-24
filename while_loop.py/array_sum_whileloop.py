array=[2,3,5,4]
sum=8
left=0
right=len(array)-1

array.sort()
is_exist=False

while(left<right):
    left_element=array[left]
    right_element=array[right]
    current_sum=left_element+right_element
    if sum==current_sum:
        print("pairs",left_element,right_element)
        is_exist=True
        break
    elif sum>current_sum:
        left+=1
    elif sum<current_sum:
        right-=1
if is_exist==False:
    print("pairs not found")                