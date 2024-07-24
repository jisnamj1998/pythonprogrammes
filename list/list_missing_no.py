arr=[5,1,2,3,4]
arr.sort()

left=0
while(left<len(arr)-1):
    right=left+1
    l_element=arr[left]
    r_element=arr[right]

    if r_element-l_element!=1:
        print(f" {l_element} is missing")
        break
    else:
        left+=1
else:
    print(r_element+1,"is missing")        
        
              