from re import *
pan_no="ABCPE9876F"
#rule="[A-Z]{3}[PCAFHT]{1}[A-Z]{1}\d{4}[A-Z]{1}"
rule="[A-Z]{3}[PCAFHT][A-Z]\d{4}[A-Z]"
matcher=fullmatch(rule,pan_no)
if (matcher==None):
    print("invalid")
else:
    print("valid")