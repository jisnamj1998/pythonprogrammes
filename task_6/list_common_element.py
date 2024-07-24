list1=[1,2,3,4,5]
list2=[5,6,7,8]
# def common_num(list1,list2):
#     result=False
#     for num in list1:
#         if num in list2:
#             result=True
#     return result
# print(common_num(list1,list2))    
for num in list1:
    if num in list2:
        result=True
        print(result)
        break
else:
    result=False
    print(result)    

        

        
        