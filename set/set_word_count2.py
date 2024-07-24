orders=["fried rice","dosa","porotta","dosa","porotta","vb","cb","vb"]



#wc={o:orders.count(o) for o in set(orders)}
#print(wc)


st_orders=set(orders)
wc={}
for o in st_orders:
    wc[o]=orders.count(o)
print(wc)
    