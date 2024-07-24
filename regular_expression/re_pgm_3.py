from re import *
text="abc J8is& 4na"
#lower case alphabet with position
#[] --> character set
#pattern="[a-z]" # check lowercase alphabets
#pattern="[A-Z]"  # CHECH UPPERCASE ALPHABETS
#pattern="[a-zA-Z]" # check all alphabets
#pattern="[0-9]"     # check digit
#pattern="[a-zA-Z0-9]" # check alphanumeric characters
#pattern="[^a-zA-Z0-9]"  #check spcl characters including space ,except alpha,nums
pattern="[abc]" #check either a,b or c
matcher=finditer(pattern,text)
count=0
for m in matcher:
    print(m.start(),m.group())
    count+=1
print(f"count of{pattern} is {count}")    
