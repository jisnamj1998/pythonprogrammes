from re import *
ph_no="9656682398"
rule="[0-9]{10}"
matcher=fullmatch(rule,ph_no)
print("invalid" if matcher==None else "valid")