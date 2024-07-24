tummy_size=int(input("enter tummy size"))
buttock_size=int(input("enter butttock size"))
gender=input("enter gender")
value=tummy_size/buttock_size
#round fn used
value=round(value,2)
if gender=="male":
    if value<0.96:
        print("low")
    elif value<1:
        print("moderate")
    elif value>=1:
        print("high")
elif gender=="female":
      if value<0.80:
          print("low")
      elif value<0.85:
          print("moderate")
      elif value>=0.85:
          print("high")                        