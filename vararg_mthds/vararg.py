# we can receive n no of args
def add_numbers(*args):
    return sum(args)
print(add_numbers(10,20))
print(add_numbers(10,20,40,50,60))

#kwargs use**

def display_student(**kwargs):
    return kwargs.get("name")
print(display_student(id="40",name="jisna",course="msc"))

#or
#def dis_stu(**kwargs)
#    print(kwargs.get("name"))
# dis_stu(id.....)




