import urllib.request, json
import pandas as pd

date='05-05-2021'

pincode='226010'

age = 45

url = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode='+pincode+'&date='+date

response = urllib.request.urlopen(url)

data = json.loads(response.read())

center = (data['centers'])
data1 = {}
for sessions in center:
    name = sessions['name']
    for key,value in sessions.items():
        if key == "sessions":
            for d in value:
                for key,value in d.items():
                    if (key=='min_age_limit' and value==age):
                        data1 = d
                        dt = data1['date']
                        for key,value in data1.items():
                            if (key=='available_capacity' and value>0):
                                print('{} Vaccine(s) is(are) available for {}+ age at {} for {}. Please book now'.format(value,age,name,dt))