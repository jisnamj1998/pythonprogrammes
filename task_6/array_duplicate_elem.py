array=[1,2,3,3,4,5,5,6]
duplicates=[]
for i in range(len(array)):
    for j in range(i+1,len(array)):
        if array[i]==array[j]:
            duplicates.append(array[i])
print(duplicates)            