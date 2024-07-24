from re import fullmatch
path="C:\\Users\\Jisna jeemoc\\python_programmes.py\\regexpro\\phnumbers.txt"
f=open(path,"r")
rule="(\+91)?\d{10}"
for line in f:
    ph_nos=line.rstrip("\n")
    matcher=fullmatch(rule,ph_nos)
    if matcher!=None:
        print(ph_nos)
    