arr=[5,1,2,4,3]
arr.sort()
left=0
while(left<len(arr)-1):
    right=left+1
    r_ele=arr[right]
    l_ele=arr[left]
    if r_ele-l_ele!=1:
        print(f"{l_ele+1} is missing" )
        break
    else:
        left=left+1
else:
    print(f"{r_ele+1} is missing")        
