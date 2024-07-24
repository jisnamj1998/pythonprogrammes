string1="ABC"
string2="PQRST"
s1_length=len(string1)
s2_length=len(string2)
smallest_length=string1 if s1_length<s2_length else string2
result=""
for i in range(0,smallest_length):
    result=result+string1[i]+string2[i]
if len(string1)>len(string2):
    rem=string1[smallest_length:]
else:
    rem=string2[smallest_length:]
print(result+rem)            


