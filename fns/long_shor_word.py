text="longest word"
words=text.split(" ")

def get_length(word):
    return len(word)
longest_word=max(words,key=get_length)
print(longest_word)

shortest_word=min(words,key=get_length)
print(shortest_word)


