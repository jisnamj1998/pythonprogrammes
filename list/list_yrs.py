years=[]
#1800-2024
century_yrs=[]
non_century_yrs=[]
for i in range(1800,2025):
    years.append(i)

for i in years:
    if i%100==0:
        century_yrs.append(i)
    else:
        non_century_yrs.append(i)
print(f"century yrs {century_yrs}")
print(f"non century yrs {non_century_yrs}")
                     