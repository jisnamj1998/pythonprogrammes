text="hello WOrld"
text=text.casefold()
def count(text):
    vowels=["a","e","i","o","u"]
    v_count=0
    for ch in text:
        if ch in vowels:
            v_count+=1
    return v_count
print(count(text))        
