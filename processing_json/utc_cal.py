from datetime import datetime,timedelta
offset_india=timedelta(hours=05.30)
print(f"offset india {offset_india}")
offset_usa=timedelta(hours=-12.00)
print(f"offset india {offset_usa}")      

time_country1=datetime.utcnow()+offset_india
print(f"first {time_country1}")
time_country2=datetime.utcnow()+offset_usa
print(f"second {time_country2}")
time_difference=time_country1-time_country2
print(time_difference.total_seconds())
time=time_difference.total_seconds()
conclusion=print("ahead") if time>0 else print("behind")
print(conclusion)