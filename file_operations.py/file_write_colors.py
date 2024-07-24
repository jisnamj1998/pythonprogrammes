lst=["red","green","yellow","blue","black","purple","brown"]
path="C:\\Users\\Jisna jeemoc\\python_programmes.py\\file_operations.py\\colors.txt"
f=open(path,"w")
for c in lst:
    f.write(c+"\n")