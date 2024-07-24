array=(2,3,5,4)
sum=8
is_present=False

for i in range(0,len(array)-1):
    for j in range(i+1,len(array)):
        i_element=array[i]
        j_element=array[j]
        current_sum=i_element+j_element
        if current_sum==sum:
            print("pairs",i_element,j_element)
            is_present=True
            break
if is_present==False:
    print(f"pairs not found")  

    #efficiency less so we prefer while loop bcoz iteratn no is more while comparing      