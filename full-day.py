import json, requests, datetime

#gulfport 
city_id = ["4450411"] # Waveland, MS; Norfolk, MS; SD 
#api_key = "SuperSecretKey" # open weather api key, should be protected
with open('api.key', 'r') as file:
    api_key = file.read().replace('\n', '')


def get_date(timezone):
    tz = datetime.timezone(datetime.timedelta(seconds=int(timezone)))
    return datetime.datetime.fromtimestamp(element["dt"], tz = tz).strftime("%Y.%m.%d-%H:%M:%S") #strftime is just for visually formatting the datetime object

for city in city_id:
    url = "https://api.openweathermap.org/data/2.5/forecast?id=%s&appid=%s&units=imperial&cnt=8" % (city, api_key)
    response  = requests.get(url)
    data = json.loads(response.text)
    for element in data["list"]:
     weather_info = {'city.id': f"{data['city']['id']}",
                     'time': f"{get_date(data['city']['timezone'])}",
                     'city': f"{data['city']['name']}",
                     'current.temperature': f"{element['main']['temp']}",
                     'heat.index': f"{element['main']['feels_like']}",
                     'condition': f"{element['weather'][0]['main']}",
                     'wind': f"{element['wind']['speed']}",
                     'pressure': f"{element['main']['pressure']}",
                     'humidity': f"{element['main']['humidity']}"
                     }
     print(weather_info)
#    print(data)
    print()
