from json import load
path="python_programmes.py//processing_json//products.json"
f=open(path,"r",encoding="UTF-8")
data=load(f)

print(len(data))

#product title
#prod_title=[p.get("title") for p in data]
#print(prod_title)

#all categories
#st=set()
#for p in data:
 #   st.add(p.get("category"))
#print(st) 
#or   
#cate=[p.get("category") for p in data]
#print(set(cate))

#all prod name under 50
#prod_under50=[p.get("title") for p in data if p.get("price")<50]
#print(prod_under50)

#cate jewe products
#jew_prod=[p.get("title")for p in data if p.get("category")=="jewelery"]
#print(jew_prod)

#costly prod
#def get_price(dictionary):
 #   return dictionary.get("price")
#costly_prod=max(data,key=get_price)
#print(costly_prod.get("title"),costly_prod.get("price"))

#cheapest prod
#cheapest_pro=min(data,key=get_price)
#print(cheapest_pro.get("title"),cheapest_pro.get("price"))

#prod title,ratings rate
#ratings_rate=[(p.get("title"),p.get("rating").get("count")) for p in data]
#print(ratings_rate)

#max rating
def max_rating_count(dictionary):
    return dictionary.get("rating").get("count")
max_rating=max(data,key=max_rating_count)
print(max_rating.get("title"),max_rating.get("rating").get("count"))



    







