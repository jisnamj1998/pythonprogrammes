text="this is a goodmorning msg"
words=text.split(" ")

def get_len(w):
    return len(w)
#lambda w:len(w)

min_word=min(words,key=get_len)
print(min_word)

max_word=max(words,key=get_len)
print(max_word)
srt_word=sorted(words,key=get_len)
print(srt_word)
desc_srt_word=sorted(words,key=get_len,reverse=True)
print(desc_srt_word)




    
   

