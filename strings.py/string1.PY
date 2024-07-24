string1="ABC"
string2="PQRST"
length1=len(string1)
result=""
for i in range(0,length1):
    result=result+string1[i]+string2[i]
remainder=string2[length1:]
result=result+remainder
print(result)    

     