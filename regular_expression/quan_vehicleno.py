from re import fullmatch
#vehicle_no="KL-09-JK-9876"
vehicle_no="KL09JK9876"
rule="(KL)[-]?\d{2}[-]?[A-Z]{1,2}[-]?\d{4}"
matcher=fullmatch(rule,vehicle_no)
if(matcher!=None):
    print("valid")
else:
    print("invalid")    