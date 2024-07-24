string="luminar"
even=[]
odd=[]
for i in string:
    if string.index(i)%2==0:
        even.append(i)
    else:
        odd.append(i)
print("even characters :- " ,even)
print("odd characters :- ",odd)