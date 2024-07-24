numbers=[3,4,8,9,7,6]
even_list=[]
odd_list=[]

for num in numbers:
    if num%2==0:
        even_list.append(num)
    else:
        odd_list.append(num)   
print(f"odd list,{odd_list}")
print(f"even list,{even_list}")         