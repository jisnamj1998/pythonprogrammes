word="madam"
result=""
length=len(word)
for i in range(length-1,-1,-1):
    result=result+word[i]
print("palindrome" if result==word else "not palindrome")    
