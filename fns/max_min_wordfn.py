def get_length(word):
    return len(word)

def min_max_word(text,is_max=True):
    words=text.split(" ")
    if is_max==True:
        longest_word=max(words,key=get_length)
        return longest_word
    else:
        shortest_word=min(words,key=get_length)
        return shortest_word
text="good morning"
#longest word
#print(min_max_word(text))  
#shortest word
print(min_max_word(text,is_max=False))      
