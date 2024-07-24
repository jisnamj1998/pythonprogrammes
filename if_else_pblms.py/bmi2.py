weight=int(input("enter weight"))
height_in_cm=int(input("enter height"))
height_in_metre=height_in_cm/100
bmi=weight/(height_in_metre**2)
print(bmi)
# if bmi<18:
#     print("underweight")
# elif 18<=bmi<25:
#     print("healthy")
# elif 25<=bmi<30:
#     print("over weight")
# elif 30<=bmi<35:
#     print("obese")
# elif 35<=bmi<40:
#     print("severe obesity")           
 

if bmi<18:
  print("under weight")
elif bmi<25:
  print("healthy")
elif bmi<30:
  print("over weight")
elif bmi<35:
  print("obese")
elif bmi<40:
  print("severe obesity")             