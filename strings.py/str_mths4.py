text="pneumonoultramicroscopicsilicovolcanoconiosis"
#print(text.count("pneumonoultramicroscopicsilicovolcanoconiosis"))
print(len(text))
# no.of voowels
#no.of consonents
vowels=("a","e","i","o","u")
v_count=0
c_count=0
for ch in text:
    if ch in vowels:
        v_count=v_count+1
    else:
        c_count=c_count+1
print(f"no of vowels={v_count} and no of consonents={c_count}")            
        