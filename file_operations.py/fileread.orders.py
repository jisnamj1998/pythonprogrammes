path="C:\\Users\\Jisna jeemoc\\python_programmes.py\\file_operations.py\\orders.txt"
f=open(path,"r")
items=[]

for line in f:
    data=line.strip("\n")
    items.append(data)
#items orderded in that day    
print(set(items))
# count of part.item
wc={i:items.count(i) for i in set(items)}
print(wc)
#max
value_key_list=[(v,k) for k,v in wc.items()]
print(max(value_key_list))
#min
print(min(value_key_list))
#sort
print(sorted(value_key_list))
#desc sort
print(sorted(value_key_list,reverse=True))

