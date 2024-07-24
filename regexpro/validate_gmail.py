from re import fullmatch
path="C:\\Users\\Jisna jeemoc\\python_programmes.py\\regexpro\\gmailid.txt"
f=open(path,"r")
rule="[a-z][a-z0-9_-]*@gmail.com"
for line in f:
    gmail_id=line.rstrip("\n")
    matcher=fullmatch(rule,gmail_id)
    if matcher!=None:
        print(gmail_id)