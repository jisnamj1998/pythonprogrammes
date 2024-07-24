from re import fullmatch
phone_no="+919656682398"
rule="(\+91)?\d{10}"  #spcl character comes \+ need to use
matcher=fullmatch(rule,phone_no)
if (matcher!=None):
    print("valid")
else:
    print("invalid")     