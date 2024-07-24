arr=[3,5,2,7,15,9,8,20]
element=int(input("enter searching element"))

arr.sort()
left=0
right=len(arr)-1


while(left<=right):
    mid=(left+right)//2

    if arr[mid]==element:
        print("element found")
        break
    elif arr[mid]<element:
        left=mid+1
    elif arr[mid]>element:
        right=mid-1

else:
    print("element not found")            

     


