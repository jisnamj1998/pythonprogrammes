from re import *
text="aaabcbbcaabaaacbaa"
#pattern="a*" #check any no.of a including zero
#pattern="a{2}" #check a exist in 2 times
pattern="a{2,3}" #chech min 2a max 3 a

matcher=finditer(pattern,text)
for m in matcher:
    print(m.start(),m.group())
