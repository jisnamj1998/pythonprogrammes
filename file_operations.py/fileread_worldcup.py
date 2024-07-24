path="C:\\Users\\Jisna jeemoc\\python_programmes.py\\file_operations.py\\worldcup.txt"

f=open(path,"r")
teams=[]
for line in f: 
    data=line.rstrip("\n").split(" ")
    teams.append(data[1])
print(teams) 
#winners
print(set(teams)) 
#count
wc={t:teams.count(t) for t in set(teams)} 
print(wc) 
#max winners
value_key_list=[(v,k) for k,v in wc.items()]
print(max(value_key_list))


