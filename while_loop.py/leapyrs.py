i=2000
while(i<=3000):
    if (i%100==0 and i%400==0)or(i%100!=0 and i%4==0):
     print(i)
    i+=1   