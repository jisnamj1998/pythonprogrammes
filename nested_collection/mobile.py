products=[
    {"code":100,"name":"redminote13","brand":"redmi","price":30000,"network":"5g"},
    {"code":101,"name":"iphone15","brand":"apple","price":130000,"network":"5g"},
    {"code":102,"name":"samsunga18","brand":"samsung","price":20000,"network":"4g"},
    {"code":103,"name":"redminote12","brand":"redmi","price":30000,"network":"4g"},
    {"code":104,"name":"s23ultra","brand":"samsung","price":150000,"network":"5g"},
    {"code":105,"name":"motoedge","brand":"motorola","price":24000,"network":"5g"},
    {"code":106,"name":"oneplus9r","brand":"oneplus","price":30000,"network":"5g"},
 
    
]
#total no of products
print(len(products))
#price of apple product

for dictionary in products:
    if dictionary.get("brand")=="apple":
        print(dictionary.get("price"))

#or
apple_price=[dictionary.get("price") for dictionary in products if dictionary.get("brand")=="apple"]
print(apple_price)         

#mobiles available 20k-25k

mobile_price=[p.get("name") for p in products if p.get("price") in range(20000,25001)]
print(mobile_price)

#costly brand
def get_price(dictionary):
    return dictionary.get("price")
costly_product=max(products,key=get_price)
print(costly_product)
print(costly_product.get("brand"))
#cheap brand
cheap_brand=min(products,key=get_price)
print(cheap_brand.get("brand"))
#mobile support 5g
five_g_products=[p.get("name") for p in products if p.get("network")=="5g"]
print(five_g_products)

#no of products in same brand
all_brands=[p.get("brand") for p in products]
wc={b:all_brands.count(b) for b in set(all_brands)}
print(wc)





    
costly_product=max(products,key=get_price)