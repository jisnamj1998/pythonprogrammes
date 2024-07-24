word=input("enter word")
length=len(word)-1
result=""
for i in range(length,-1,-1):
    result=result+word[i]
print("palindrome" if result==word else "not palindrome") 

