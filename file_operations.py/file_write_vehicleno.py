vehicle_numbers=["KL-08-CD-9987","TN-23-GH-9876","KA-32-JK-5647","AP-43-CD-9876","KL-09-JK-5443","TN-56-YT-6545"]
path="C:\\Users\\Jisna jeemoc\\python_programmes.py\\file_operations.py\\vehicle_no.txt"
f=open(path,"w")
#kl reg nos only
for num in vehicle_numbers:
    if num.startswith("KL"):
        f.write(num+"\n")
