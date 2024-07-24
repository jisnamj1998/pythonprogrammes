from json import load
path="C:\\Users\\Jisna jeemoc\\python_programmes.py\\processing_json\\restcountries.json"
f=open(path,"r",encoding="UTF-8")
data=load(f)

#print no.of countries
print(len(data))

#country names
country_name=[c.get("name") for c in data]
print(country_name)

#which country's capital is Hanoi
country_hanoi=[c.get("name") for c in data if c.get("capital")=="Hanoi"]
print(country_hanoi)

#all countries capital
capitals=[c.get("capital") for c in data]
print(capitals)

#highest population country
def max_population(dictionary):
    return dictionary.get("population")
highest_population=max(data,key=max_population)
print(highest_population.get("name"))
#or
#lambda dictionary:dictionary.get("population")#or
#highest_population=max(data,key=lambda dictionary:dictionary.get("population"))

#smallest population
smallest_population=min(data,key=max_population)
print(smallest_population)

#china (CHN) bordered countries
border_china=[c.get("name")for c in data if "borders" in c and "CHN" in c.get("borders")]
print(border_china)

#border_name=[c.get("name") for c in data if "CHN" in c.get("borders",[])]
#print(border_name)


#indpt countries
indpt_countries=[c.get("name") for c in data if c.get("independant")=="true"]
print(indpt_countries)

#dpnd countries
dpnd_countries=[c.get("name") for c in data if c.get("independant")=="false"]
print(dpnd_countries)

#timezone of vietnam
timezone=[c.get("timezone")for c in data if c.get("name")=="Vietnam"]
print(timezone)

#Wallis and Futuna altSpellings
spelling=[c.get("altSpellings") for c in data if c.get("name")=="Wallis and Futuna"]
print(spelling)

#png of flags in Wallis and Futuna
flags=[c.get("flags").get("png") for c in data if c.get("name")=="Wallis and Futuna"]
print(flags)

#country name with languages
values={}
for c in data:
    lang=[]
    if "languages" in c:
        for l in c.get("languages"):
            lang.append(l.get("name"))
        values[c.get("name")]=lang
print(values)            

#country with indian rupee
for c in data:
    if "currencies" in c:
        for cur in c.get("currencies"):
            if cur.get("name")=="Indian Rupee":
                print(c.get("name"))

#all countries with multiple timezone
timezone=[c.get("name") for c in data if len(c.get("timezones"))>1]
print(timezone)

#country starts with A
countries=[c.get("name") for c in data if c.get("name").startswith("A")]
print(countries)

#region count
#asia:?
region=[c.get("region")for c in data]
wc={r:region.count(r) for r in region} 
print(wc)  


#timezone ahead or behind
#UTC+ AHEAD ,UTC- BEHIND
timezone_india=[c.get("timezones")for c in data if c.get("name")=="India"]
india_timezone=timezone_india[0][0]
timezone_afg=[c.get("timezones") for c in data if c.get("name")=="Afghanistan"]
afg_timezone=timezone_afg[0][0]
#to remove utc and replace : with.
india_offset=india_timezone.lstrip("UTC").replace(":",".")
print(india_offset)
afg_offset=afg_timezone.lstrip("UTC").replace(":",".")
print(afg_offset)
from datetime import datetime,timedelta
offset_india=timedelta(hours=5.30)
print(f"offset india {offset_india}")
offset_afg=timedelta(hours=4.30)
print(f"offset india {afg_offset}")      

time_country1=datetime.utcnow()+offset_india
print(f"first {time_country1}")
time_country2=datetime.utcnow()+offset_afg
print(f"second {time_country2}")
time_difference=time_country1-time_country2
print(time_difference.total_seconds())
time=time_difference.total_seconds()
conclusion=print("ahead") if time>0 else print("behind")
print(conclusion)




