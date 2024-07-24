string="A2B4C6"
alpha=[]
digit=[]
for t in string:
    if t.isalpha():
        alpha.append(t)
    else:
        digit.append(t)
result="".join(alpha+digit)
print("sorted string :- ",result)