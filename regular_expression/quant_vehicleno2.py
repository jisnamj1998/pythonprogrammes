from re import *
vehicle_no="KL09RS6523"
rule="(KL)[0-9]{2}[A-Z]{1,2}[0-9]{4}"
matcher=fullmatch(rule,vehicle_no)
if(matcher==None):
    print("invalid")
else:
    print("valid")    