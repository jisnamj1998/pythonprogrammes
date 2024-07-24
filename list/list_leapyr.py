years=[]
leap_yrs=[]
for y in range(1800,2025):
    years.append(y)
for y in years:
    if (y%100==0 and y%400==0) or (y%100!=0 and y%4==0):
        leap_yrs.append(y)
print(leap_yrs)  
print(f"no.of leap yrs,{len(leap_yrs)}")         