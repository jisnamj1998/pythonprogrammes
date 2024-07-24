languages=["python","c++","c","java","javascript","typescript"]

new_list=[]
for lang in languages:
    new_list.append(lang.upper())
print(new_list) 

# comprehension mthd  
#new_list=[lang.upper() for lang in languages]
#print(new_list)

#name count>5 filter out
#length_filter=[lang for lang in languages if len(lang)>5]
#print(length_filter)

list=[2,4,6,3,1]
#num>5 num+1 num<5 num-1

new_list=[num+1 if num>5 else num-1  for num in list ]
print(new_list)

list=["+","-","+","+","-","+","+","-"]
map_list=[1 if symb=="+" else 0 for symb in list]
print(map_list)



