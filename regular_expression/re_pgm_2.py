from re import *
text="Pam has a cat. The cat is fat. The fat cat is black. Black fat cat sat in the jam. Pam has a rag bag. In the bag went Black Fat Cat. Dad and Pam ran with Black Fat Cat to the tap."
pattern="am"
matcher=finditer(pattern,text)
count=0
for m in matcher:
    print(m.start(),m.group())
    count+=1
print(f"count of {pattern}={count}")   

pattern1="ag"
count=0
matcher1=finditer(pattern1,text)
for m in matcher1:
    print(m.start(),m.group())
    count+=1
print(f"count of {pattern1}={count}")    


