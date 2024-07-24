from re import *
date_is="01"
rule="(0[1-9]|[12][0-9]|3[01])"
matcher=fullmatch(rule,date_is)
if (matcher==None):
    print("invalid")
else:
    print("valid")    