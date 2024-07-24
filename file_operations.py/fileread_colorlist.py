path="C:\\Users\\Jisna jeemoc\\python_programmes.py\\file_operations.py\\colors.txt"
f=open(path,"r")
color_list=[]
for line in f:
    color_list.append(line.rstrip("\n"))
print(color_list)

#color_list=[line.rstrip("\n") for line in f]
#print(color_list)

print(set(color_list))