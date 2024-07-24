arr1=[1,2,3,4,5]
arr2=[3,4,5,6]
# def add(arr1,arr2):

#     s=0
#     for num in arr1:
#       if num in arr2:
#         s=s+num
#     return s
# print(add([1,2,3,4,5],[3,4,5,6]))     


#or
def common_sum(arr1,arr2):
    wc={num:arr1.count(num) for num in set(arr2)}
    total=sum([k for k,v in wc.items() if v>0])
    return total
print(common_sum(arr1,arr2))
       