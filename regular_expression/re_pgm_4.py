from re import *
text="fatboy@2K2#"
#pattern="\d" #check digit
#pattern="\D" #exclude digit [^0-9]
#pattern="\w"  #alphanumeric
#pattern="\W" # spcl chrctr [^a-zA-Z0-9]
#"\s" to get space
#"\S" to exclude space



matcher=finditer(pattern,text)
for m in matcher:
    print(m.start(),m.group())

