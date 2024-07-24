from re import *
text="fat cat tom ran very fast to catch jerry"
pattern="at"
matcher=finditer(pattern,text)
count=0
for m in matcher:
    print(m.start(),m.group())
    count+=1
print(f"occurance of {pattern}={count}")    
