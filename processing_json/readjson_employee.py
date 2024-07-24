from json import load
path="C:\\Users\\Jisna jeemoc\\python_programmes.py\\processing_json\\employee.json"
f=open(path,"r")
employees=load(f)

#print(employees)

#no.of employees
print(len(employees))

#employee names
#for e in employees:
#    print(e.get("name"))
#or
emp_name=[e.get("name") for e in employees]
print(emp_name)

#employee name working as qa
qa_emp=[e.get("name") for e in employees if e.get("department")=="qa"]
print(qa_emp)

#locatn ekm employees
ekm_emp=[e.get("name") for e in employees if e.get("location")=="ekm"]
print(ekm_emp)