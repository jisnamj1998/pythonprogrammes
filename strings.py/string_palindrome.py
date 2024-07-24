word="hello"
# for i in range(4,-1,-1):
#     print(word[i])

result=""
for i in range(4,-1,-1):
    result=result+word[i]
print(result)

print("palindrome" if result==word else "not palindrome")
