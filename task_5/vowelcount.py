text="hellopython"
vowels=["a","e","i","o","u"]
wc={ch:text.count(ch) for ch in set(text) if ch in vowels}
print(wc)