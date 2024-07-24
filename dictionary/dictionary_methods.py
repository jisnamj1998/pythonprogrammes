course={"name":"django","language":"python","duration":7,"fees":5000,"faculty":"shyam"}

#keys()
#for k in course.keys():
#    print(k)

#values()
#for v in course.values():
#    print(v)

#items()
#for k,v in course.items():
# print(k,v)     

#get()
#print(course.get("fees")) 

#print(course["fees"])

#update()
course.update({"fees":6000})
print(course)
course.update({"duration":8,"faculty":"jisna"})
print(course)

#pop()
course.pop("faculty")
print(course)

