def unique_string(text):
    common_characters=[]
    for ch in text:
        if ch not in common_characters:
            common_characters.append(ch)
    return ("").join(common_characters)#list to string type
print(unique_string("helloworld"))
        
