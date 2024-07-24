#1800-2024
from re import fullmatch
yr="2019"
#rule="(18[0-9]{2}|19[0-9]{2}|20[01][0-9]|20(2)[0-4])"
#rule="(18|19)[0-9]{2}|20[01][0-9]|202[0-4]"
rule="(1)[89][0-9]{2}|20[01][0-9]|202[0-4]"
matcher=fullmatch(rule,yr)
if (matcher==None):
    print("invalid")
else:
    print("valid")    
