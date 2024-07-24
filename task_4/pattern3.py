for row in range(1,5):
    for column in range(1,row+1):
        print("*",end="\t")
    print("\n")
for row in range(5,0,-1):
    for column in range(1,row+1):
        print("*",end="\t")
    print("\n")                