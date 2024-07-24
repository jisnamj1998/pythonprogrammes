from re import fullmatch
path="C:\\Users\\Jisna jeemoc\\python_programmes.py\\regexpro\\tyreno.txt"
f=open(path,"r")
rule="\d{3}/\d{2}/R\d{2}/\d{2}[a-z]"
for line in f:
    tyreno=line.rstrip("\n")
    matcher=fullmatch(rule,tyreno)
    if matcher!=None:
        print(tyreno)
