from flask import Flask, request, jsonify, render_template
import json, datetime, sys, urllib.request

app = Flask(__name__)

def cowin_api(idx):
    d=datetime.datetime.now()
    date=d.strftime("%d-%m-%Y")
    district_id=idx
    age = 18
    #url = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByPin?pincode='+pincode+'&date='+date
    url = 'https://cdn-api.co-vin.in/api/v2/appointment/sessions/public/calendarByDistrict?district_id='+district_id+'&date='+date
    #print(url)
    response = urllib.request.urlopen(url)
    data = json.loads(response.read())
    #print(data)
    center = (data['centers'])
    data1 = {}
    list1 = []
    for sessions in center:
        name = sessions['name']
        for key,value in sessions.items():
            if key == "sessions":
                for d in value:
                    for key,value in d.items():
                        if (key=='min_age_limit' and value==int(age)):
                            data1 = d
                            dt = data1['date']
                            for key,value in data1.items():
                                if (key=='available_capacity' and value>0):
                                    #print('{} Vaccine(s) is(are) available for {}+ age at {} for {}. Please book now.'.format(value,age,name,dt))
                                    list1.append('{} Vaccine(s) is(are) available for {}+ age at {} for {}. Please book now.'.format(value,age,name,dt))
    #print(list1)
    dictOfWords = { i : list1[i] for i in range(0, len(list1) ) }
    #print (dictOfWords)
    return dictOfWords

    
@app.route('/')
@app.route('/<idx>')
@app.route('/index')
def co_api(idx=670):
    dict1 = cowin_api(str(idx))
    #print(dict1)
    return render_template('index.html', dict1=dict1)