from re import *
month_is="04"
rule="(0[1-9]|1[012])"
matcher=fullmatch(rule,month_is)
if (matcher==None):
    print("invalid")
else:
    print("valid")    