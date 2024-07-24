def upper_lower(string):
    upper=0
    lower=0
    for ch in string:
        if ch.islower():
            lower+=1
        if ch.isupper():
            upper+=1
    return lower,upper
string="PaLAkkAD"
l,u=upper_lower(string)
print("lowercases count",l)
print("uppercases",u)
                   
