expenses={"jan":1200,"feb":1300,"mar":1400,"apr":1500}
print(expenses["mar"])
#list
#print(expenses[2]) index no use here in dicti key value using

product={"code":314,"name":"kurta","category":"XL","price":500}
print(product["name"])
#insert color=black
product["color"]="black"
print(product)
#update price=600
product["price"]=600
print(product)
#check offer key present or not
print("offer" in product)
#add offer as 300 if offer key is not present  else update offer as 250
if "offer" in product:
    product["offer"]=250
else:
    product["offer"]=300
print(product)        
