from re import fullmatch
path="C:\\Users\\Jisna jeemoc\\python_programmes.py\\regexpro\\panno.txt"
f=open(path,"r")
rule="[A-Z]{3}[PCAFHT][A-Z]\d{4}[A-Z]"
for line in f:
    pan_no=line.rstrip("\n")
    matcher=fullmatch(rule,pan_no)
    if matcher!=None:
        print(pan_no)
