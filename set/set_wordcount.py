text="goodmorning"
set_text=set(text)
wc={}
for ch in set_text:
    wc[ch]=text.count(ch)
print(wc)    

# word count by converting to set type to avoid duplicates
# dictionary coprehension
wc={ch:text.count(ch) for ch in set(text)}
print(wc)