#json file to python format
from json import load
path="C:\\Users\\Jisna jeemoc\\python_programmes.py\\processing_json\\students.json"
f=open(path,"r")
data=load(f)

#for dictionary in data:
    #print(dictionary.get("name"))
    #print(dictionary.get("place"))

#    if dictionary.get("place")=="thrissur":
#        print(dictionary.get("name")

#place_filter=[dictionary.get("name") for dictionary in data if dictionary.get("place"=="thrissur")]
#print(place_filter)


#courses
course_set=set()
for dictionary in data:
    course_set.add(dictionary.get("course"))
print(course_set)


#unpacking
dict_1={1:"one",2:"two",3:"three"}
dict_2={4:"four"}
new_dict={**dict_1,**dict_2}
print(new_dict)
    
    
        
                
    
    